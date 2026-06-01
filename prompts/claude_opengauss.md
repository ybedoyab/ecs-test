Seccion 3.2 openGauss solamente. IDs `g1_1`, `g1_2`, `g2_1`, etc. (una subtarea = un TASK).

Recursos tipicos (validar en el PDF):
- ECS nombre `ict-opengauss`, IP privada `192.168.0.228`, imagen compartida `ict-opengauss`, openEuler 22.03 ARM, 8 vCPU / 16 GiB, disco 60 GB, VPC `vpc-default` o la del enunciado.
- Base: usuario `omm`, puerto `26000`, postgres DB para administracion.

Genera SQL completo cuando el PDF define tablas:
- Tablespace: ruta `/opt/opengauss/tablespaces/ts_supplychain` con `mkdir`, `chown omm:dbgrp`, `chmod 700`, y `CREATE TABLESPACE ... LOCATION '...'`.
- BD `db_supplychain` UTF8 en `ts_supplychain`, `\c` o equivalente.
- Tablas supplier, part, lineitem, orders con columnas, tipos y constraints del PDF (PRIMARY KEY, FOREIGN KEY, NOT NULL).
- Datos INSERT del enunciado si los lista.
- Migracion, consultas, roles/usuarios, audit: comandos y SQL literales del procedimiento (gsql, `\du`, políticas RLS, parámetros de performance si aparecen).

Cada subtarea con su captura exacta (`1-1-1create_ts`, `1-2-1create_change_db`, etc.). No resumas varias capturas en un bloque.

Prohibido: "ejecutar SQL segun enunciado" sin el SQL; "crear tablas necesarias" sin DDL.
