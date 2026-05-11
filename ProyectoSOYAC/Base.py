import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import time
import threading


# ----------------------------
# Clase Proceso
# ----------------------------
class Proceso:
    def __init__(self, nombre, tiempo):
        self.nombre = nombre
        self.tiempo = tiempo
        self.tiempo_restante = tiempo
        self.estado = "Listo"


# ----------------------------
# Sistema Operativo GUI
# ----------------------------
class SistemaOperativoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Sistema Operativo Básico")
        self.root.geometry("780x590")
        self.root.resizable(False, False)

        self.root.configure(bg="#ECECEC")

        self.procesos = []

        # ---------- Estilos ----------
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white")

        style.configure("Treeview.Heading",
                        font=("Arial", 10, "bold"),
                        background="#4A90E2",
                        foreground="white")

        style.map("Treeview",
                  background=[("selected", "#B3D9FF")])

        style.configure("TProgressbar",
                        thickness=20)

        # ---------- Título ----------
        titulo = tk.Label(root,
                          text="SIMULADOR DE SISTEMA OPERATIVO",
                          font=("Arial", 18, "bold"),
                          bg="#ECECEC",
                          fg="#2C3E50")
        titulo.pack(pady=15)

        # ---------- Frame Crear Proceso ----------
        frame_crear = tk.Frame(root, bg="#D6EAF8", bd=2, relief="groove")
        frame_crear.pack(pady=10, padx=20, fill="x")

        tk.Label(frame_crear, text="Nombre:", font=("Arial", 10, "bold"),
                 bg="#D6EAF8", fg="#154360").grid(row=0, column=0, padx=10, pady=10)

        self.entry_nombre = tk.Entry(frame_crear, width=18)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame_crear, text="Tiempo:", font=("Arial", 10, "bold"),
                 bg="#D6EAF8", fg="#154360").grid(row=0, column=2, padx=10, pady=10)

        self.entry_tiempo = tk.Entry(frame_crear, width=10)
        self.entry_tiempo.grid(row=0, column=3, padx=10, pady=10)

        btn_crear = tk.Button(frame_crear,
                              text="Crear Proceso",
                              font=("Arial", 10, "bold"),
                              bg="#3498DB",
                              fg="white",
                              activebackground="#2E86C1",
                              relief="flat",
                              command=self.crear_proceso)
        btn_crear.grid(row=0, column=4, padx=20, pady=10)

        # ---------- Tabla ----------
        frame_tabla = tk.Frame(root, bg="#ECECEC")
        frame_tabla.pack(pady=10)

        self.tabla = ttk.Treeview(frame_tabla, columns=("Nombre", "Tiempo", "Restante", "Estado"), show="headings", height=12)
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Tiempo", text="Tiempo")
        self.tabla.heading("Restante", text="Restante")
        self.tabla.heading("Estado", text="Estado")

        self.tabla.column("Nombre", width=200)
        self.tabla.column("Tiempo", width=120)
        self.tabla.column("Restante", width=120)
        self.tabla.column("Estado", width=200)

        self.tabla.pack()

        # ---------- Botones ----------
        frame_botones = tk.Frame(root, bg="#F2F3F4", bd=2, relief="groove")
        frame_botones.pack(pady=15, padx=20, fill="x")

        btn_eliminar = tk.Button(frame_botones,
                                 text="Eliminar",
                                 width=12,
                                 font=("Arial", 10, "bold"),
                                 bg="#E74C3C",
                                 fg="white",
                                 activebackground="#C0392B",
                                 relief="flat",
                                 command=self.eliminar_proceso)
        btn_eliminar.grid(row=0, column=0, padx=10, pady=10)

        btn_fcfs = tk.Button(frame_botones,
                             text="Ejecutar FCFS",
                             width=14,
                             font=("Arial", 10, "bold"),
                             bg="#27AE60",
                             fg="white",
                             activebackground="#229954",
                             relief="flat",
                             command=self.iniciar_fcfs)
        btn_fcfs.grid(row=0, column=1, padx=10, pady=10)

        btn_rr = tk.Button(frame_botones,
                           text="Ejecutar RR",
                           width=14,
                           font=("Arial", 10, "bold"),
                           bg="#8E44AD",
                           fg="white",
                           activebackground="#7D3C98",
                           relief="flat",
                           command=self.iniciar_rr)
        btn_rr.grid(row=0, column=2, padx=10, pady=10)

        btn_reset = tk.Button(frame_botones,
                              text="Reiniciar",
                              width=14,
                              font=("Arial", 10, "bold"),
                              bg="#F39C12",
                              fg="white",
                              activebackground="#D68910",
                              relief="flat",
                              command=self.reiniciar_procesos)
        btn_reset.grid(row=0, column=3, padx=10, pady=10)

        # ---------- Barra de progreso ----------
        self.progress = ttk.Progressbar(root, length=600, mode="determinate")
        self.progress.pack(pady=10)

        # ---------- Label Porcentaje ----------
        self.label_porcentaje = tk.Label(root,
                                         text="Progreso: 0%",
                                         font=("Arial", 10, "bold"),
                                         bg="#ECECEC",
                                         fg="#2C3E50")
        self.label_porcentaje.pack()

        # ---------- Estado ----------
        self.label_estado = tk.Label(root,
                                     text="Estado: Esperando acción del usuario...",
                                     font=("Arial", 11, "bold"),
                                     bg="#ECECEC",
                                     fg="#1F618D")
        self.label_estado.pack(pady=10)

    # ----------------------------
    # Actualizar tabla
    # ----------------------------
    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for p in self.procesos:
            self.tabla.insert("", "end", values=(p.nombre, p.tiempo, p.tiempo_restante, p.estado))

    # ----------------------------
    # Actualizar porcentaje
    # ----------------------------
    def actualizar_porcentaje(self, ejecutado, total):
        if total == 0:
            porcentaje = 0
        else:
            porcentaje = int((ejecutado / total) * 100)

        self.label_porcentaje.config(text=f"Progreso: {porcentaje}%")

    # ----------------------------
    # Crear proceso
    # ----------------------------
    def crear_proceso(self):
        nombre = self.entry_nombre.get().strip()
        tiempo = self.entry_tiempo.get().strip()

        if nombre == "" or tiempo == "":
            messagebox.showerror("Error", "Debes llenar el nombre y el tiempo.")
            return

        for p in self.procesos:
            if p.nombre.lower() == nombre.lower():
                messagebox.showerror("Error", "Ya existe un proceso con ese nombre.")
                return

        try:
            tiempo = int(tiempo)
            if tiempo <= 0:
                messagebox.showerror("Error", "El tiempo debe ser mayor que 0.")
                return
        except:
            messagebox.showerror("Error", "El tiempo debe ser un número.")
            return

        self.procesos.append(Proceso(nombre, tiempo))
        self.entry_nombre.delete(0, tk.END)
        self.entry_tiempo.delete(0, tk.END)

        self.label_estado.config(text="Estado: Proceso creado correctamente.", fg="#117A65")
        self.actualizar_tabla()

    # ----------------------------
    # Eliminar proceso
    # ----------------------------
    def eliminar_proceso(self):
        seleccionado = self.tabla.selection()

        if not seleccionado:
            messagebox.showwarning("Aviso", "Selecciona un proceso para eliminar.")
            return

        item = self.tabla.item(seleccionado)
        nombre = item["values"][0]

        for p in self.procesos:
            if p.nombre == nombre:
                self.procesos.remove(p)
                break

        self.label_estado.config(text="Estado: Proceso eliminado.", fg="#B03A2E")
        self.actualizar_tabla()

    # ----------------------------
    # Reiniciar procesos
    # ----------------------------
    def reiniciar_procesos(self):
        for p in self.procesos:
            p.estado = "Listo"
            p.tiempo_restante = p.tiempo

        self.progress["value"] = 0
        self.label_porcentaje.config(text="Progreso: 0%")

        self.label_estado.config(text="Estado: Procesos reiniciados.", fg="#1F618D")
        self.actualizar_tabla()

    # ----------------------------
    # Iniciar FCFS (hilo)
    # ----------------------------
    def iniciar_fcfs(self):
        if len(self.procesos) == 0:
            messagebox.showwarning("Aviso", "No hay procesos para ejecutar.")
            return

        hilo = threading.Thread(target=self.ejecutar_fcfs)
        hilo.start()

    # ----------------------------
    # Ejecutar FCFS
    # ----------------------------
    def ejecutar_fcfs(self):
        self.label_estado.config(text="Estado: Ejecutando FCFS...", fg="#27AE60")

        total = sum(p.tiempo_restante for p in self.procesos)
        if total == 0:
            total = 1

        ejecutado = 0
        self.progress["value"] = 0
        self.progress["maximum"] = total
        self.actualizar_porcentaje(ejecutado, total)

        for p in self.procesos:
            if p.tiempo_restante <= 0:
                p.estado = "Terminado"
                continue

            p.estado = "Ejecutando"
            self.actualizar_tabla()

            while p.tiempo_restante > 0:
                time.sleep(1)
                p.tiempo_restante -= 1
                ejecutado += 1

                self.progress["value"] = ejecutado
                self.actualizar_porcentaje(ejecutado, total)
                self.actualizar_tabla()
                self.root.update_idletasks()

            p.estado = "Terminado"
            self.actualizar_tabla()

        self.progress["value"] = total
        self.actualizar_porcentaje(total, total)

        self.label_estado.config(text="Estado: FCFS finalizado.", fg="#2C3E50")

    # ----------------------------
    # Iniciar Round Robin
    # ----------------------------
    def iniciar_rr(self):
        if len(self.procesos) == 0:
            messagebox.showwarning("Aviso", "No hay procesos para ejecutar.")
            return

        quantum = simpledialog.askinteger("Quantum", "Ingresa el quantum (segundos):", minvalue=1)

        if quantum is None:
            return

        hilo = threading.Thread(target=self.ejecutar_rr, args=(quantum,))
        hilo.start()

    # ----------------------------
    # Ejecutar RR
    # ----------------------------
    def ejecutar_rr(self, quantum):
        self.label_estado.config(text="Estado: Ejecutando Round Robin...", fg="#8E44AD")

        total = sum(p.tiempo_restante for p in self.procesos)
        if total == 0:
            total = 1

        ejecutado = 0
        self.progress["value"] = 0
        self.progress["maximum"] = total
        self.actualizar_porcentaje(ejecutado, total)

        procesos_pendientes = True

        while procesos_pendientes:
            procesos_pendientes = False

            for p in self.procesos:
                if p.tiempo_restante > 0:
                    procesos_pendientes = True
                    p.estado = "Ejecutando"
                    self.actualizar_tabla()

                    ejecutar = min(quantum, p.tiempo_restante)

                    for _ in range(ejecutar):
                        time.sleep(1)
                        p.tiempo_restante -= 1
                        ejecutado += 1

                        self.progress["value"] = ejecutado
                        self.actualizar_porcentaje(ejecutado, total)
                        self.actualizar_tabla()
                        self.root.update_idletasks()

                    if p.tiempo_restante == 0:
                        p.estado = "Terminado"
                    else:
                        p.estado = "Listo"

                    self.actualizar_tabla()

        self.progress["value"] = total
        self.actualizar_porcentaje(total, total)

        self.label_estado.config(text="Estado: Round Robin finalizado.", fg="#2C3E50")


# ----------------------------
# Programa principal
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaOperativoGUI(root)
    root.mainloop()