create database gimnasio;
use gimnasio;
create table rol (
    idRol int(25) not null,
    descripcion varchar(25) not null,
    constraint pk_rol primary key (idRol)
)ENGINE-InnoDb;


create table persona(
    idPersona int(25) auto_increment not null,
     idRol int(25) not null,
    dni int(30) not null,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    sexo varchar(1) check(sexo = 'F' or sexo = 'M'),
    tel varchar(20) null,
    email varchar(60) null
    constraint pk_persona primary key (idPersona),
    constraint uq_tel unique (tel),
    constraint uq_email unique (email),
    constraint uq_dni unique (dni),
    constraint fk_rol foreign key (idRol) references rol (idRol)
)ENGINE-InnoDb;

create table actividad(

)