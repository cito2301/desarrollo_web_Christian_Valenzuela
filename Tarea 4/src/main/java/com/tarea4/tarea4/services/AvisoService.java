package com.tarea4.tarea4.services;

import com.tarea4.tarea4.models.AvisoAdopcion;
import com.tarea4.tarea4.repositories.AvisoRepository;
import com.tarea4.tarea4.repositories.NotaRepository;
import com.tarea4.tarea4.ver.AvisoVer;

import org.springframework.stereotype.Service;

import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

@Service
public class AvisoService {
    private final AvisoRepository avisoRepo;
    private final NotaRepository notaRepo;
    private final DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd");

    public AvisoService(AvisoRepository avisoRepo, NotaRepository notaRepo) {
        this.avisoRepo = avisoRepo;
        this.notaRepo = notaRepo;
    }

    public List<AvisoVer> getAllAvisosView() {
        List<AvisoAdopcion> avisos = avisoRepo.findAllByOrderByFechaIngresoAsc();
        List<AvisoVer> out = new ArrayList<>();
        for (AvisoAdopcion a : avisos) {
            AvisoVer v = new AvisoVer();
            v.id = a.getId();
            v.fechaStr = a.getFechaIngreso() == null ? "" : a.getFechaIngreso().format(fmt);
            v.sector = (a.getSector() == null || a.getSector().isBlank()) ? "No especifica" : a.getSector();
            v.cantidad = a.getCantidad();
            v.tipo = a.getTipo() == null ? "" : a.getTipo().name();
            
            Integer edad = a.getEdad();
            if (edad == null) edad = 0;

            String unidad = (a.getUnidadMedida() == null) ? "" : a.getUnidadMedida().name();

            if ("m".equalsIgnoreCase(unidad)) {
                v.edadStr = edad + (edad == 1 ? " mes" : " meses");
            } else {
                v.edadStr = edad + (edad == 1 ? " año" : " años");
            }

            v.comuna = (a.getComuna() == null) ? "" : a.getComuna().getNombre();
            Double avg = notaRepo.findAverageByAvisoId(a.getId());
            v.promedioNota = (avg == null) ? null : Math.round(avg * 100.0) / 100.0;
            v.contadorNotas = notaRepo.countByAviso_Id(a.getId());
            out.add(v);
        }
        return out;
    }
}
