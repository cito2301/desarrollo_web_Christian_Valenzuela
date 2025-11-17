package com.tarea4.tarea4.repositories;

import com.tarea4.tarea4.models.AvisoAdopcion;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface AvisoRepository extends JpaRepository<AvisoAdopcion, Integer> {
    List<AvisoAdopcion> findAllByOrderByFechaIngresoAsc();
}
