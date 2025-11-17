package com.tarea4.tarea4.services;

import com.tarea4.tarea4.models.*;
import com.tarea4.tarea4.repositories.AvisoRepository;
import com.tarea4.tarea4.repositories.NotaRepository;

import org.springframework.stereotype.Service;

@Service
public class NotaService {

    private final NotaRepository notaRepository;
    private final AvisoRepository avisoRepository;

    public NotaService(NotaRepository notaRepository, AvisoRepository avisoRepository) {
        this.notaRepository = notaRepository;
        this.avisoRepository = avisoRepository;
    }

    public double agregarNota(Integer avisoId, Integer notaValor) {
        AvisoAdopcion aviso = avisoRepository.findById(avisoId).orElseThrow();
        Nota n = new Nota();
        n.setNota(notaValor);
        n.setAviso(aviso);
        notaRepository.save(n);

        return notaRepository.findByAviso_Id(avisoId)
                .stream()
                .mapToInt(Nota::getNota)
                .average()
                .orElse(-1);
    }
}
