#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# il modulo "main" di avvio.

from mod.pwd_generator import * # Importo il programma all'interno del modulo "pwd_generator", e specifico il package "lib" relativo alla directory contenente il programma.
import sys
import compileall # La libreria "compileall" compila tutti i moduli presenti nella directory "lib" in Bytecode.

# Compila tutti i moduli presenti nella cartella "mod"
# generando i Bytecode nella sottocartella "__pychace__".
# Compilando il Bytecode lo aggiorna in automatico.
compileall.compile_dir('mod/')

# Creo la classe principale "Main" che racchiude la funzione per l'avvio del programma principale.
class Main:
        def __init__(self): # Funzione che contiene il metodo "self".
                self.name = 'pwd_generator' # Avvio del modulo principale dove risiede il programma.
                
# Sarà sufficiente cancellare tutti i moduli .py e pyw (eccetto __init__.pyw)
# per distribuire il programma già pseudo-compilato senza il codice sorgente.
