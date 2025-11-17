package com.tarea4.tarea4.repositories;

import com.tarea4.tarea4.models.Nota;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import java.util.List;


public interface NotaRepository extends JpaRepository<Nota, Integer> {
    List<Nota> findByAviso_Id(Integer avisoId);
    @Query("SELECT AVG(n.nota) FROM Nota n WHERE n.aviso.id = :avisoId")
    Double findAverageByAvisoId(@Param("avisoId") Integer avisoId);

    long countByAviso_Id(Integer avisoId);
}
