package com.tarea4.tarea4.controllers;

import com.tarea4.tarea4.services.AvisoService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class AvisoController {
    private final AvisoService avisoService;
    public AvisoController(AvisoService avisoService) {
        this.avisoService = avisoService;
    }

    @GetMapping("/avisos")
    public String listaAvisos(Model model) {
        model.addAttribute("avisos", avisoService.getAllAvisosView());
        return "avisos";
    }

    @GetMapping("/")
    public String index() {
        return "redirect:/avisos";
    }
}
