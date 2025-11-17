package com.tarea4.tarea4.models;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "aviso_adopcion")
public class AvisoAdopcion {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "fecha_ingreso")
    private LocalDateTime fechaIngreso;

    @ManyToOne
    @JoinColumn(name = "comuna_id")
    private Comuna comuna;

    @Column(name = "sector")
    private String sector;

    @Column(name = "nombre")
    private String nombre;

    @Column(name = "email")
    private String email;

    @Column(name = "celular")
    private String celular;

    @Enumerated(EnumType.STRING)
    @Column(name = "tipo")
    private TipoAnimal tipo;

    public TipoAnimal getTipo() { return tipo; }

    @Column(name = "cantidad")
    private Integer cantidad;

    @Column(name = "edad")
    private Integer edad;

    @Enumerated(EnumType.STRING)
    @Column(name = "unidad_medida")
    private UnidadMedida unidadMedida;

    public UnidadMedida getUnidadMedida() { return unidadMedida; }
    public void setUnidadMedida(UnidadMedida unidadMedida) { this.unidadMedida = unidadMedida; }

    @Column(name = "fecha_entrega")
    private LocalDateTime fechaEntrega;

    @Column(name = "descripcion", length = 500)
    private String descripcion;

    public AvisoAdopcion() {}
    public Integer getId() { return id; }
    public LocalDateTime getFechaIngreso() { return fechaIngreso; }
    public Comuna getComuna() { return comuna; }
    public String getSector() { return sector; }
    public Integer getCantidad() { return cantidad; }
    public Integer getEdad() { return edad; }
    public void setFechaIngreso(LocalDateTime fechaIngreso) { this.fechaIngreso = fechaIngreso; }
    public void setComuna(Comuna comuna) { this.comuna = comuna; }
}
