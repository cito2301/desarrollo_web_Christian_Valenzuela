package com.tarea4.tarea4.models;

import jakarta.persistence.*;

@Entity
@Table(name = "nota")
public class Nota {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @ManyToOne
    @JoinColumn(name = "aviso_id")
    private AvisoAdopcion aviso;

    @Column(name = "nota")
    private Integer nota;

    public Nota() {}
    public Nota(AvisoAdopcion aviso, Integer nota) {
        this.aviso = aviso;
        this.nota = nota;
    }
    public Integer getId() { return id; }
    public AvisoAdopcion getAviso() { return aviso; }
    public void setAviso(AvisoAdopcion aviso) { this.aviso = aviso; }
    public Integer getNota() { return nota; }
    public void setNota(Integer nota) { this.nota = nota; }
}
