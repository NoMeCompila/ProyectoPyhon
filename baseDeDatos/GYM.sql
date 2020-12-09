create database  gimnasio;
use gimnasio;
create table rol (
    idRol int identity not null,
    descripcion varchar(25) not null,
    constraint pk_rol primary key (idRol)
);


create table persona(
    idPersona int identity not null,
    idRol int not null,
    dni int not null,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    sexo varchar(1),
    tel varchar(20) null,
    email varchar(60) null,
    constraint pk_persona primary key (idPersona),
    constraint uq_tel unique (tel),
    constraint uq_email unique (email),
    constraint uq_dni unique (dni),
    constraint fk_rol foreign key (idRol) references rol (idRol),
	constraint chk_email check (email like '%@%.com')
);

create table  actividad(
    idActividad int identity not null,
    descripcion varchar (20) not null,
    constraint uq_descripcion unique(descripcion),
    constraint pk_activiad primary key (idActividad)
);

create table ventas_cabecera(
    idVCabecera int identity not null,
    idPersona int not null,
    fecha date,
    total float,
    constraint pk_ventas_cabecera primary key (idVCabecera),
    constraint fk_ventas_persona foreign key (idPersona) references persona(idPersona)
);

create table ventas_detalle(
    idVDetalle int identity not null,
    idVCabecera int not null,
    idActividad int not null,
    fecha_expiracion date,
    constraint pk_ventas_detalle primary key (idVDetalle),
    constraint fk_ventas_detalle_cabecera foreign key (idVCabecera) references ventas_cabecera(idVCabecera),
    constraint fk_ventas_detalle_actividad foreign key (idActividad) references actividad(idActividad)
);

create table estado(
    idPersona int not null,
    idActividad int not null,
    idEstado int identity not null,
    estado bit not null,
    constraint fk_persona foreign key (idPersona) references persona(idPersona),
    constraint fk_actividad foreign key (idActividad) references actividad(idActividad),
    constraint pk_estado primary key (idPersona,idActividad,idEstado)
);

INSERT INTO rol (descripcion) VALUES ('Admin');
INSERT INTO rol (descripcion) VALUES ('Owner');
INSERT INTO rol (descripcion) VALUES ('Instructor');

select * from rol