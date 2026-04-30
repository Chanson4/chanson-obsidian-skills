#!/usr/bin/env python3
"""Create a learning vault directory structure from a JSON specification."""
import json
import sys
from pathlib import Path


def title_from_filename(path: str) -> str:
    name = Path(path).name
    if name.endswith('.md'):
        name = name[:-3]
    return name


def main() -> int:
    if len(sys.argv) != 2:
        print('Usage: python create_vault_structure.py spec.json')
        return 2
    spec_path = Path(sys.argv[1])
    spec = json.loads(spec_path.read_text(encoding='utf-8'))
    vault_path = Path(spec['vault_path']).expanduser().resolve()
    root = spec.get('root', '')
    base = (vault_path / root).resolve()
    overwrite = bool(spec.get('overwrite', False))
    created_folders = []
    created_files = []
    skipped_existing = []
    errors = []
    try:
        base.mkdir(parents=True, exist_ok=True)
        created_folders.append(str(base))
    except Exception as exc:
        errors.append({'path': str(base), 'error': str(exc)})
    for item in spec.get('items', []):
        rel = item.get('path', '').strip('/ ')
        if not rel:
            continue
        kind = item.get('type') or ('file' if rel.endswith('.md') else 'folder')
        target = (base / rel).resolve()
        try:
            if kind == 'folder':
                if target.exists():
                    skipped_existing.append(str(target))
                else:
                    target.mkdir(parents=True, exist_ok=False)
                    created_folders.append(str(target))
            elif kind == 'file':
                target.parent.mkdir(parents=True, exist_ok=True)
                if target.exists() and not overwrite:
                    skipped_existing.append(str(target))
                else:
                    template = item.get('template')
                    if template is None:
                        template = '# ' + title_from_filename(rel) + '\n'
                    target.write_text(template, encoding='utf-8')
                    created_files.append(str(target))
            else:
                errors.append({'path': str(target), 'error': 'unknown item type: ' + str(kind)})
        except Exception as exc:
            errors.append({'path': str(target), 'error': str(exc)})
    result = {
        'created_folders': created_folders,
        'created_files': created_files,
        'skipped_existing': skipped_existing,
        'errors': errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
