Seccion 3.1 openEuler solamente. Cada subtarea del PDF = un `<!-- TASK:tM_N -->`.

Recursos tipicos de este examen (confirma y ajusta con el texto del PDF si difiere):
- ECS `ecs-1` (nodo contenedor): openEuler 22.03 ARM, 4 vCPU, 8 GiB, disco 40 GB, IP `192.168.0.101/24`.
- ECS `ecs-2` (almacenamiento NFS): mismas specs, IP `192.168.0.102/24`.
- Console: Pay-per-use, Kunpeng, flavor tipo `kc1.xlarge.2`, imagen openEuler 22.03 ARM 64bit, VPC segun topologia, EIP traffic 50 Mbit/s si aplica.

Incluye en copy:
- Backup yum: `cd /etc/yum.repos.d/` y copia a `.bak`.
- Upgrade: `sed` de `22.03-LTS` a `24.03-LTS-SP2`, `dnf -y update releasever='24.03LTS-SP2' --allowerasing --skip-broken`, `reboot`, `uname -a`.
- iSula: install, `daemon.json` con registry-mirrors y CNI (`network-plugin`, `cni-bin-dir`, `cni-conf-dir`), `git clone https://gitee.com/yftyxa/cni_for_i-sulad_arm.git`, paths `/opt/bin/cni`, `/etc/cni/net.d`.
- NFS en ecs-2: `/nfs/share`, `shared.html`, linea exports con cliente `192.168.0.101(rw,async,no_root_squash)`, `exportfs -v`.
- Cliente ecs-1: `mount -t nfs 192.168.0.102:/nfs/share /nfs/client`.
- Nginx/isula: red `cni-nginx`, contenedores `nginx1`/`nginx2`, puertos 8081/8082, volumenes desde `/nfs/client/web1` y `web2`, LB en `/tmp/nginx-lb.conf` si el PDF lo pide.

No dejes pasos de consola Huawei sin campos concretos.
