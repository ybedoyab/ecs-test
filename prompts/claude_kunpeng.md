Seccion 3.3 Kunpeng solamente. IDs `k1_1`, `k1_2`, `k2_1`, etc.

Recursos tipicos (validar en el PDF):
- ECS `ecs-standalone`, Kunpeng ARM, openEuler 22.03 64bit, 4 vCPU 8 GiB, disco 60 GB, imagen compartida `ict-kunpeng`.
- Trabajo en `/home/kunpeng` con paquetes del enunciado.

Console (task 1.1): pasos numerados con flavor Kunpeng, imagen compartida ICT-kunpeng/ict-kunpeng, disco 60 GB, red/EIP segun tabla — sin frases vagas.

Terminal detallado:
- `dnf install -y gcc-c++ cmake` + verificacion `g++ --version`, `cmake --version`.
- DevKit: `tar -xzf DevKit-All-25.0.0-Linux-Kunpeng.tar.gz`, `cd DevKit-All-25.0.0-Linux-Kunpeng`, `bash install.sh` (o ruta del PDF), acceso WebUI `https://<EIP>:puerto` con usuario `devadmin` y `{tu_contrasena}`.
- Porting Advisor: menus exactos, tipo Source Code Porting, target openEuler AArch64, analisis de `spdlog-1.11.0.zip`.
- spdlog: `unzip`, `mkdir build && cd build`, `cmake ..`, `make`, rutas de parches si el PDF las da.
- KML: `rpm -ivh kml-2.3.0-1.aarch64.rpm`, edicion completa de `CMakeLists.txt` con includes/libs del PDF, `cmake`, `make`, ejecutable en `KML_BLAS_Project/build`.

Usa rutas absolutas bajo `/home/kunpeng/...`. No `<ruta_proyecto>` ni "segun tabla Cloud Resources".
