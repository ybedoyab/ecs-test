# regional_2526

<!-- SECTION:openeuler -->
<!-- TASK:t1_1 -->
# Task 1.1 — Upgrade OS kernel (ecs-1)

step:
copy:
```
cp -a /etc/yum.repos.d /etc/yum.repos.d.bak
```
captura: 1-1-1b

step:
copy:
```
sed -i 's/22.03-LTS/24.03-LTS-SP2/g' /etc/yum.repos.d/openEuler.repo
```
captura: 1-1-2yum

step:
copy:
```
uname -a
```
captura: 1-1-3uname1

step:
copy:
```
dnf -y update releasever='24.03LTS-SP2' --allowerasing --skip-broken
```
captura: 1-1-4kernel

step:
copy:
```
reboot
uname -a
```
captura: 1-1-5uname2
<!-- END:t1_1 -->

<!-- TASK:t1_2 -->
# Task 1.2 — Build container node iSula (ecs-1)

step:
copy:
```
dnf install -y iSulad
systemctl enable --now isulad
```
captura: 1-2-1isula

step:
copy:
```
isula pull nginx
```
captura: 1-2-2repo

step:
copy:
```
isula images
```
captura: 1-2-3pull

step:
copy:
```
dnf install -y git
git clone https://gitee.com/yftyxa/cni_for_i-sulad_arm.git
```
captura: 1-2-4git

step:
copy:
```
mkdir -p /opt/bin/cni /etc/cni/net.d
cp cni_for_i-sulad_arm/* /opt/bin/cni/
```
captura: 1-2-5cni

step:
copy:
```
systemctl restart isulad
```
captura: 1-2-6config
<!-- END:t1_2 -->

<!-- TASK:t2_1 -->
# Task 2.1 — NFS shared storage server (ecs-2)

step:
copy:
```
mkdir -p /nfs/share
```
captura: 2-1-1share

step:
copy:
```
echo 'This is shared data' > /nfs/share/shared.html
cat /nfs/share/shared.html
```
captura: 2-1-2shared-data

step:
copy:
```
echo '/nfs/share 192.168.0.101(rw,async,no_root_squash)' >> /etc/exports
cat /etc/exports
```
captura: 2-1-3rule

step:
copy:
```
systemctl enable --now nfs-server
```
captura: 2-1-4start

step:
copy:
```
exportfs -v
```
captura: 2-1-5export
<!-- END:t2_1 -->

<!-- TASK:t2_2 -->
# Task 2.2 — NFS client mount (ecs-1)

step:
copy:
```
mkdir -p /nfs/client
mount -t nfs 192.168.0.102:/nfs/share /nfs/client
```
captura: 2-2-1mount

step:
copy:
```
cat /nfs/client/shared.html
```
captura: 2-2-2share
<!-- END:t2_2 -->

<!-- TASK:t3_1 -->
# Task 3.1 — Web directories on shared storage (ecs-2)

step:
copy:
```
mkdir -p /nfs/share/web1 /nfs/share/web2
ls /nfs/share/
```
captura: 3-1-1webdir

step:
copy:
```
echo 'This is webnode1' > /nfs/share/web1/index.html
echo 'This is webnode2' > /nfs/share/web2/index.html
cat /nfs/share/web1/index.html /nfs/share/web2/index.html
```
captura: 3-1-2index

step:
copy:
```
cat /nfs/share/web1/index.html
cat /nfs/share/web2/index.html
```
captura: 3-1-3verify
<!-- END:t3_1 -->
<!-- END:openeuler -->
