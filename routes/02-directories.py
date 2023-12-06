from pathlib import Path

path = Path("routes")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("mundo-feliz")

for p in path.iterdir():
    print(p)
    
archivos = [p for p in path.iterdir() if not p.is_dir()]
print(archivos)

archivos_py = [p for p in path.glob("*.py")]
print(archivos_py)

archivos_01py = [p for p in path.glob("*01-*.py")]
print(archivos_01py)

archivos_x_py = [p for p in path.glob("**/*.py")]
print(archivos_x_py)

archivos_r_py = [p for p in path.rglob("*.py")]
print(archivos_r_py)