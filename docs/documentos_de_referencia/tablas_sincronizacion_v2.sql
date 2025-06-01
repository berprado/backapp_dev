--
-- Set default database
--
USE adminerp_copy;

--
-- Create table `sincronizarparametricaunidadmedida`
--
CREATE TABLE sincronizarparametricaunidadmedida
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoClasificador    VARCHAR(10)  NOT NULL,
    descripcion           VARCHAR(255) DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 127,
AVG_ROW_LENGTH = 130,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create index `codigoClasificador` on table `sincronizarparametricaunidadmedida`
--
ALTER TABLE sincronizarparametricaunidadmedida
ADD UNIQUE INDEX codigoClasificador (codigoClasificador);

--
-- Create table `sincronizarparametricatiposfactura`
--
CREATE TABLE sincronizarparametricatiposfactura
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoClasificador    VARCHAR(10)  NOT NULL,
    descripcion           VARCHAR(255) DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 5,
AVG_ROW_LENGTH = 4096,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create index `codigoClasificador` on table `sincronizarparametricatiposfactura`
--
ALTER TABLE sincronizarparametricatiposfactura
ADD UNIQUE INDEX codigoClasificador (codigoClasificador);

--
-- Create table `sincronizarparametricatipopuntoventa`
--
CREATE TABLE sincronizarparametricatipopuntoventa
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoClasificador    VARCHAR(10)  NOT NULL,
    descripcion           VARCHAR(255) DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 7,
AVG_ROW_LENGTH = 2730,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create index `codigoClasificador` on table `sincronizarparametricatipopuntoventa`
--
ALTER TABLE sincronizarparametricatipopuntoventa
ADD UNIQUE INDEX codigoClasificador (codigoClasificador);

--
-- Create table `sincronizarparametricatipomoneda`
--
CREATE TABLE sincronizarparametricatipomoneda
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoClasificador    VARCHAR(10)  NOT NULL,
    descripcion           VARCHAR(255) DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 155,
AVG_ROW_LENGTH = 106,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create index `codigoClasificador` on table `sincronizarparametricatipomoneda`
--
ALTER TABLE sincronizarparametricatipomoneda
ADD UNIQUE INDEX codigoClasificador (codigoClasificador);

--
-- Create table `sincronizarparametricatipometodopago`
--
CREATE TABLE sincronizarparametricatipometodopago
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoClasificador    VARCHAR(10)  NOT NULL,
    descripcion           VARCHAR(255) DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 307,
AVG_ROW_LENGTH = 214,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create index `codigoClasificador` on table `sincronizarparametricatipometodopago`
--
ALTER TABLE sincronizarparametricatipometodopago
ADD UNIQUE INDEX codigoClasificador (codigoClasificador);

--
-- Create table `sincronizarparametricatipohabitacion`
--
CREATE TABLE sincronizarparametricatipohabitacion
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoClasificador    VARCHAR(10)  NOT NULL,
    descripcion           VARCHAR(255) DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 17,
AVG_ROW_LENGTH = 1024,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create index `codigoClasificador` on table `sincronizarparametricatipohabitacion`
--
ALTER TABLE sincronizarparametricatipohabitacion
ADD UNIQUE INDEX codigoClasificador (codigoClasificador);

--
-- Create table `sincronizarparametricatipoemision`
--
CREATE TABLE sincronizarparametricatipoemision
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoClasificador    VARCHAR(10)  NOT NULL,
    descripcion           VARCHAR(255) DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 5,
AVG_ROW_LENGTH = 4096,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create index `codigoClasificador` on table `sincronizarparametricatipoemision`
--
ALTER TABLE sincronizarparametricatipoemision
ADD UNIQUE INDEX codigoClasificador (codigoClasificador);

--
-- Create table `sincronizarparametricatipodocumentosector`
--
CREATE TABLE sincronizarparametricatipodocumentosector
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoClasificador    VARCHAR(10)  NOT NULL,
    descripcion           VARCHAR(255) DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 52,
AVG_ROW_LENGTH = 321,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create index `codigoClasificador` on table `sincronizarparametricatipodocumentosector`
--
ALTER TABLE sincronizarparametricatipodocumentosector
ADD UNIQUE INDEX codigoClasificador (codigoClasificador);

--
-- Create table `sincronizarparametricatipodocumentoidentidad`
--
CREATE TABLE sincronizarparametricatipodocumentoidentidad
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoClasificador    VARCHAR(10)  NOT NULL,
    descripcion           VARCHAR(255) DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 6,
AVG_ROW_LENGTH = 3276,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create index `codigoClasificador` on table `sincronizarparametricatipodocumentoidentidad`
--
ALTER TABLE sincronizarparametricatipodocumentoidentidad
ADD UNIQUE INDEX codigoClasificador (codigoClasificador);

--
-- Create table `sincronizarparametricapaisorigen`
--
CREATE TABLE sincronizarparametricapaisorigen
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoClasificador    VARCHAR(10)  NOT NULL,
    descripcion           VARCHAR(255) DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 212,
AVG_ROW_LENGTH = 77,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create index `codigoClasificador` on table `sincronizarparametricapaisorigen`
--
ALTER TABLE sincronizarparametricapaisorigen
ADD UNIQUE INDEX codigoClasificador (codigoClasificador);

--
-- Create table `sincronizarparametricamotivoanulacion`
--
CREATE TABLE sincronizarparametricamotivoanulacion
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoClasificador    VARCHAR(10)  NOT NULL,
    descripcion           VARCHAR(255) DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 5,
AVG_ROW_LENGTH = 4096,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create index `codigoClasificador` on table `sincronizarparametricamotivoanulacion`
--
ALTER TABLE sincronizarparametricamotivoanulacion
ADD UNIQUE INDEX codigoClasificador (codigoClasificador);

--
-- Create table `sincronizarparametricaeventossignificativos`
--
CREATE TABLE sincronizarparametricaeventossignificativos
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoClasificador    VARCHAR(10)  NOT NULL,
    descripcion           VARCHAR(255) DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 8,
AVG_ROW_LENGTH = 2340,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create index `codigoClasificador` on table `sincronizarparametricaeventossignificativos`
--
ALTER TABLE sincronizarparametricaeventossignificativos
ADD UNIQUE INDEX codigoClasificador (codigoClasificador);

--
-- Create table `sincronizarlistaproductosservicios`
--
CREATE TABLE sincronizarlistaproductosservicios
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoActividad       VARCHAR(20)  NOT NULL,
    codigoProducto        VARCHAR(20)  NOT NULL,
    descripcionProducto   VARCHAR(255) DEFAULT NULL,
    nandina               TEXT         DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 273,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create index `unique_codigo` on table `sincronizarlistaproductosservicios`
--
ALTER TABLE sincronizarlistaproductosservicios
ADD UNIQUE INDEX unique_codigo (codigoActividad, codigoProducto);

--
-- Create table `sincronizarlistamensajesservicios`
--
CREATE TABLE sincronizarlistamensajesservicios
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoClasificador    VARCHAR(10)  NOT NULL,
    descripcion           VARCHAR(255) DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 193,
AVG_ROW_LENGTH = 256,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create index `codigoClasificador` on table `sincronizarlistamensajesservicios`
--
ALTER TABLE sincronizarlistamensajesservicios
ADD UNIQUE INDEX codigoClasificador (codigoClasificador);

--
-- Create table `sincronizarlistaleyendasfactura`
--
CREATE TABLE sincronizarlistaleyendasfactura
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoActividad       VARCHAR(255) DEFAULT NULL,
    descripcionLeyenda    VARCHAR(255) DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 33,
AVG_ROW_LENGTH = 512,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create table `sincronizarlistaactividadesdocumentosector`
--
CREATE TABLE sincronizarlistaactividadesdocumentosector
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoActividad       VARCHAR(10)  NOT NULL,
    codigoDocumentoSector INT(11)      NOT NULL,
    tipoDocumentoSector   VARCHAR(255) DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 25,
AVG_ROW_LENGTH = 682,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create index `codigoActividad` on table `sincronizarlistaactividadesdocumentosector`
--
ALTER TABLE sincronizarlistaactividadesdocumentosector
ADD UNIQUE INDEX codigoActividad (codigoActividad, codigoDocumentoSector);

--
-- Create table `sincronizaractividades`
--
CREATE TABLE sincronizaractividades
  (
    id                    INT(11)      NOT NULL AUTO_INCREMENT,
    codigoCaeb            VARCHAR(10)  NOT NULL,
    descripcion           VARCHAR(255) DEFAULT NULL,
    tipoActividad         VARCHAR(255) DEFAULT NULL,
    fecha_creacion        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_sincronizacion  TIMESTAMP    NULL DEFAULT NULL,
    estado_sincronizacion VARCHAR(10)  DEFAULT NULL,
    PRIMARY KEY (id)
  )
ENGINE = INNODB,
AUTO_INCREMENT = 5,
AVG_ROW_LENGTH = 4096,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_unicode_ci,
ROW_FORMAT = COMPACT;

--
-- Create index `codigoCaeb` on table `sincronizaractividades`
--
ALTER TABLE sincronizaractividades
ADD UNIQUE INDEX codigoCaeb (codigoCaeb);