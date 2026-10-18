import os
import zipfile

def package_project():
    output_zip = 'public/pockettrack-source-code.zip'
    os.makedirs('public', exist_ok=True)
    
    # Excluded directories and file patterns
    exclude_dirs = {'node_modules', 'dist', '.git', '.aistudio', '__pycache__'}
    exclude_files = {'pockettrack-source-code.zip', '.DS_Store', 'bun.lock'}
    
    print(f"Creating zip file: {output_zip}")
    count = 0
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk('.'):
            # Prune excluded directories in-place
            dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith('.')]
            
            for f in files:
                if f in exclude_files or f.endswith('.log') or f.endswith('.pyc'):
                    continue
                filepath = os.path.join(root, f)
                # Store relative path inside zip with root folder 'pockettrack/'
                arcname = os.path.join('pockettrack', os.path.relpath(filepath, '.'))
                zf.write(filepath, arcname)
                count += 1
                
    file_size_kb = os.path.getsize(output_zip) / 1024
    print(f"Successfully packaged {count} files into {output_zip} ({file_size_kb:.1f} KB)")

if __name__ == '__main__':
    package_project()
