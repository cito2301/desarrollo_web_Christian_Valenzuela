package com.tarea4.tarea4.controllers;

import com.tarea4.tarea4.models.AvisoAdopcion;
import com.tarea4.tarea4.models.Nota;
import com.tarea4.tarea4.repositories.AvisoRepository;
import com.tarea4.tarea4.repositories.NotaRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/avisos")
public class NotaApiController {
    private final AvisoRepository avisoRepo;
    private final NotaRepository notaRepo;

    public NotaApiController(AvisoRepository avisoRepo, NotaRepository notaRepo) {
        this.avisoRepo = avisoRepo;
        this.notaRepo = notaRepo;
    }

    @PostMapping("/{id}/nota")
    public ResponseEntity<?> addNota(@PathVariable("id") Integer avisoId, @RequestBody Map<String, Object> body) {
        Object nobj = body.get("nota");
        if (nobj == null) {
            return ResponseEntity.badRequest().body(Map.of("ok", false, "error", "nota_missing"));
        }
        int notaVal;
        try {
            if (nobj instanceof Number) notaVal = ((Number) nobj).intValue();
            else notaVal = Integer.parseInt(nobj.toString());
        } catch (Exception e) {
            return ResponseEntity.badRequest().body(Map.of("ok", false, "error", "nota_invalid"));
        }
        if (notaVal < 1 || notaVal > 7) {
            return ResponseEntity.badRequest().body(Map.of("ok", false, "error", "nota_range"));
        }

        AvisoAdopcion aviso = avisoRepo.findById(avisoId).orElse(null);
        if (aviso == null) return ResponseEntity.status(404).body(Map.of("ok", false, "error", "aviso_not_found"));

        Nota nota = new Nota(aviso, notaVal);
        notaRepo.save(nota);
        Double avg = notaRepo.findAverageByAvisoId(avisoId);
        long cnt = notaRepo.countByAviso_Id(avisoId);

        Map<String, Object> resp = new HashMap<>();
        resp.put("ok", true);
        resp.put("promedio", avg == null ? null : Math.round(avg * 100.0) / 100.0);
        resp.put("contador", cnt);
        return ResponseEntity.ok(resp);
    }
}
