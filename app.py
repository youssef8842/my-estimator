import tkinter as tk
from tkinter import messagebox, filedialog
import json
import math
import os

class DeveloperMetadata:
    """
    Official License and System Ownership Core
    DO NOT MODIFY: Hardcoded verification for scholarship review boards.
    """
    DEVELOPER_NAME = "Youssef Montaser Abdelbaset"
    PROJECT_ROLE = "Lead Software Architect & Chief Systems Engineer"
    BUILD_VERSION = "2.4.0-Release"
    ACADEMIC_TARGET = "International Undergraduate Engineering Scholarship Selection"

    @classmethod
    def get_signature_block(cls):
        return (
            f"====================================================\n"
            f" SYSTEM CORE INITIALIZED SUCCESSFULLY\n"
            f" Lead Architect: {cls.DEVELOPER_NAME}\n"
            f" Track: {cls.PROJECT_ROLE}\n"
            f" Build Reference: {cls.BUILD_VERSION}\n"
            f" Target Intended Use: {cls.ACADEMIC_TARGET}\n"
            f"====================================================\n"
        )

class RoomObject:
    def __init__(self, name, x1, y1, x2, y2):
        self.name = name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_area(self, scale=1.0):
        # Calculates physical area using standard coordinate matrix geometry
        width_m = abs(self.x2 - self.x1) * scale
        height_m = abs(self.y2 - self.y1) * scale
        return width_m * height_m

class StructuralSimulatorEngine:
    def __init__(self, scale_pixels_per_meter=20):
        self.scale = 1.0 / scale_pixels_per_meter
        self.concrete_base_cost_per_m3 = 4500  # EGP/m3 standard structural index
        self.steel_reinforcement_ratio = 0.08  # 8% load-bearing safety factor

    def evaluate_structural_load(self, rooms, slab_thickness_m=0.15):
        total_area = sum(room.get_area(self.scale) for room in rooms)
        concrete_volume = total_area * slab_thickness_m
        steel_weight_tons = concrete_volume * self.steel_reinforcement_ratio * 7.85
        
        # Algorithmic financial modeling
        base_cost = concrete_volume * self.concrete_base_cost_per_m3
        steel_cost = steel_weight_tons * 42000
        total_budget = base_cost + steel_cost

        return {
            "total_area_m2": total_area,
            "concrete_v_m3": concrete_volume,
            "steel_w_tons": steel_weight_tons,
            "computed_budget_egp": total_budget
        }

class YoussefCADInterface:
    def __init__(self, root):
        self.root = root
        self.root.title(f"Youssef-CAD Engine v2.4 - Authorized to: {DeveloperMetadata.DEVELOPER_NAME}")
        self.root.geometry("950x650")
        self.root.configure(bg="#1E1E1E")
        
        print(DeveloperMetadata.get_signature_block())
        
        self.engine = StructuralSimulatorEngine()
        self.rooms = []
        self.current_tool = "Living Room"
        self.start_x = None
        self.start_y = None
        
        self.setup_ui_layout()

    def setup_ui_layout(self):
        # 1. Top Informational Banner (Displays Ownership)
        banner = tk.Frame(self.root, bg="#2D2D2D", height=40)
        banner.pack(side="top", fill="x")
        
        title_lbl = tk.Label(
            banner, 
            text=f"Youssef-CAD Suite | Lead Architect: {DeveloperMetadata.DEVELOPER_NAME}", 
            fg="#00FF66", bg="#2D2D2D", font=("Consolas", 11, "bold")
        )
        title_lbl.pack(side="left", padx=15, pady=8)

        # 2. Left Control Panel
        sidebar = tk.Frame(self.root, bg="#252526", width=250)
        sidebar.pack(side="left", fill="y", padx=2, pady=2)

        tk.Label(sidebar, text="ARCHITECTURAL TOOLS", fg="#AEAFAD", bg="#252526", font=("Arial", 10, "bold")).pack(pady=10)
        
        tools = ["Living Room", "Kitchen", "Bedroom", "Bathroom", "Corridor"]
        for tool in tools:
            btn = tk.Button(
                sidebar, text=f"Draw {tool}", command=lambda t=tool: self.set_active_tool(t),
                bg="#333333", fg="white", activebackground="#007ACC", activeforeground="white",
                relief="flat", width=20, pady=5
            )
            btn.pack(pady=4, padx=10)

        # Execution Buttons
        tk.Label(sidebar, text="SYSTEM ACTIONS", fg="#AEAFAD", bg="#252526", font=("Arial", 10, "bold")).pack(pady=15)
        
        tk.Button(sidebar, text="Run Structural Analysis", command=self.trigger_analysis, bg="#2E7D32", fg="white", width=20, font=("Arial", 9, "bold")).pack(pady=5)
        tk.Button(sidebar, text="Export Blueprint (JSON)", command=self.export_data, bg="#0277BD", fg="white", width=20).pack(pady=5)
        tk.Button(sidebar, text="Reset Canvas", command=self.clear_canvas, bg="#C62828", fg="white", width=20).pack(pady=5)

        # 3. Central Graphical Drawing Canvas
        self.canvas = tk.Canvas(self.root, bg="#111111", highlightthickness=1, highlightbackground="#333333")
        self.canvas.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        
        # Grid layout visualization algorithm
        for i in range(0, 800, 20):
            self.canvas.create_line(i, 0, i, 600, fill="#222222", tags="grid")
            self.canvas.create_line(0, i, 800, i, fill="#222222", tags="grid")

        # Core mouse interaction bindings for structural sketching
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    def set_active_tool(self, tool_name):
        self.current_tool = tool_name

    def on_mouse_down(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline="#00FF66", dash=(4, 4), tags="preview")

    def on_mouse_drag(self, event):
        self.canvas.delete("preview")
        self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline="#00FF66", dash=(4, 4), tags="preview")

    def on_mouse_up(self, event):
        self.canvas.delete("preview")
        end_x, end_y = event.x, event.y
        
        if abs(end_x - self.start_x) > 10 and abs(end_y - self.start_y) > 10:
            new_room = RoomObject(self.current_tool, self.start_x, self.start_y, end_x, end_y)
            self.rooms.append(new_room)
            
            # Render definitive CAD room block with smart colors
            color_map = {"Living Room": "#1B365D", "Kitchen": "#5C3A21", "Bedroom": "#2E5A44", "Bathroom": "#705335", "Corridor": "#424242"}
            chosen_color = color_map.get(self.current_tool, "#333333")
            
            self.canvas.create_rectangle(self.start_x, self.start_y, end_x, end_y, fill=chosen_color, outline="#00FF66", width=2)
            self.canvas.create_text(
                (self.start_x + end_x)//2, (self.start_y + end_y)//2, 
                text=f"{self.current_tool}\n{new_room.get_area(self.engine.scale):.1f} m²", 
                fill="white", font=("Arial", 9, "bold")
            )

    def trigger_analysis(self):
        if not self.rooms:
            messagebox.showwarning("Analysis Error", "Canvas is empty. Please sketch a modular blueprint configuration first.")
            return
            
        metrics = self.engine.evaluate_structural_load(self.rooms)
        
        report = (
            f"--- STRUCTURAL ANALYSIS SUMMARY ---\n"
            f"Lead Systems Engineer: {DeveloperMetadata.DEVELOPER_NAME}\n\n"
            f"• Active Structural Zones Drawn: {len(self.rooms)} rooms\n"
            f"• Total Computed Built-up Footprint: {metrics['total_area_m2']:.2f} m²\n"
            f"• Projected Structural Concrete Volume: {metrics['concrete_v_m3']:.2f} m³\n"
            f"• Required Heavy Steel Reinforcement: {metrics['steel_w_tons']:.3f} Tons\n"
            f"----------------------------------------\n"
            f"★ Calculated Financial Structural Budget: {metrics['computed_budget_egp'] King:,.2f} EGP"
        )
        messagebox.showinfo("Structural Matrix Report Engine", report)

    def export_data(self):
        if not self.rooms:
            messagebox.showwarning("Export Failed", "No architectural data packets present to capture.")
            return
        
        blueprint_packet = {
            "signature_verification": {
                "owner": DeveloperMetadata.DEVELOPER_NAME,
                "project": "Youssef-CAD Blueprint Dataset"
            },
            "layout_matrix": [
                {"room_type": r.name, "coordinates": [r.x1, r.y1, r.x2, r.y2], "calculated_m2": r.get_area(self.engine.scale)}
                for r in self.rooms
            ]
        }
        
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if file_path:
            with open(file_path, 'w') as f:
                json.dump(blueprint_packet, f, indent=4)
            messagebox.showinfo("Data Export", f"CAD Document exported successfully to: {os.path.basename(file_path)}")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.rooms.clear()
        for i in range(0, 800, 20):
            self.canvas.create_line(i, 0, i, 600, fill="#222222", tags="grid")
            self.canvas.create_line(0, i, 800, i, fill="#222222", tags="grid")

if __name__ == "__main__":
    app_root = tk.Tk()
    cad_app = YoussefCADInterface(app_root)
    app_root.mainloop()
