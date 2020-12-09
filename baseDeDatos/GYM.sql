create database if not exists gimnasio;
use gimnasio;
create table rol (
    idRol int(25) not null,
    descripcion varchar(25) not null,
    constraint pk_rol primary key (idRol)
)ENGINE=InnoDb;


create table persona(
    idPersona int(25) auto_increment not null,
    idRol int(25) not null,
    dni int(30) not null,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    sexo varchar(1) check(sexo = 'F' or sexo = 'M'),
    tel varchar(20) null,
    email varchar(60) null,
    constraint pk_persona primary key (idPersona),
    constraint uq_tel unique (tel),
    constraint uq_email unique (email),
    constraint uq_dni unique (dni),
    constraint fk_rol foreign key (idRol) references rol (idRol)
)ENGINE=InnoDb;

create table actividad(
    idActividad int not null,
    descripcion varchar (20) not null,
    constraint uq_descripcion unique(descripcion),
    constraint pk_activiad primary key (idActividad)
)ENGINE=InnoDb;

create table ventas_cabecera(
    idVCabecera int auto_increment not null,
    idPersona int not null,
    fecha date,
    total float,
    constraint pk_ventas_cabecera primary key (idVCabecera),
    constraint fk_ventas_persona foreign key (idPersona) references persona(idPersona)
)ENGINE=InnoDb;

create table ventas_detalle(
    idVDetalle int auto_increment not null,
    idVCabecera int not null,
    idActividad int not null,
    fecha_expiracion date,
    constraint pk_ventas_detalle primary key (idVDetalle),
    constraint fk_ventas_detalle_cabecera foreign key (idVCabecera) references ventas_cabecera(idVCabecera),
    constraint fk_ventas_detalle_actividad foreign key (idActividad) references actividad(idActividad)
)ENGINE=InnoDb;

create table estado(
    idPersona int(25) not null,
    idActividad int not null,
    idEstado int not null,
    estado bit not null,
    constraint fk_persona foreign key (idPersona) references persona(idPersona),
    constraint fk_actividad foreign key (idActividad) references actividad(idActividad),
    constraint pk_estado primary key (idPersona,idActividad,idEstado)
)ENGINE=InnoDb;
