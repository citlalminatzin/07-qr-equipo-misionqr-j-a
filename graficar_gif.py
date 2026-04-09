import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import pi, sin

# Importamos las herramientas que ya programamos en main.py
from main import linspace, interpolate

def eval_poly(coefs: list[float], x: float) -> float:
    """Evalúa un polinomio dado sus coeficientes en un punto x"""
    return sum(c * (x ** i) for i, c in enumerate(coefs))

def generar_gif():
    # Preparamos la figura de matplotlib
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Generamos puntos finos para que las líneas se vean suaves
    x_fine = list(linspace(0, 2 * pi, 400))
    y_sine = [sin(x) for x in x_fine]
    
    # Trazamos la función seno real al fondo (estática y punteada)
    ax.plot(x_fine, y_sine, 'b--', label="sin(x) real", alpha=0.6)
    
    # Creamos los objetos gráficos vacíos que vamos a actualizar en cada frame
    line_interp, = ax.plot([], [], 'r-', label="Polinomio interpolador")
    points_plot, = ax.plot([], [], 'ko', markersize=4, label="Puntos")
    
    # Configuramos los ejes
    ax.set_xlim(-0.5, 2 * pi + 0.5)
    # IMPORTANTE: Fijamos el eje Y entre -3 y 3. 
    # Si no lo hacemos, cuando n se acerque a 100 el polinomio explotará
    # a valores gigantescos y la gráfica se deformará.
    ax.set_ylim(-3, 3)
    ax.legend(loc="upper right")
    ax.grid(True, linestyle=":", alpha=0.7)
    
    def update(frame):
        n = frame
        
        # 1. Obtenemos los n puntos y sus valores en y
        pts = list(linspace(0, 2 * pi, n))
        vals = [sin(p) for p in pts]
        
        # 2. Resolvemos el sistema M c = y para obtener coeficientes
        coefs = interpolate(pts, vals)
        
        # 3. Evaluamos el polinomio resultante en nuestra malla fina
        y_interp = [eval_poly(coefs, x) for x in x_fine]
        
        # 4. Actualizamos la línea y los puntos en la gráfica
        line_interp.set_data(x_fine, y_interp)
        points_plot.set_data(pts, vals)
        
        ax.set_title(f"Interpolación de $\sin(x)$ con $n = {n}$ puntos")
        return line_interp, points_plot

    print("Calculando factorizaciones QR y generando fotogramas...")
    print("Esto puede tomar unos segundos debido a la complejidad O(n^3)...")
    
    # Creamos la animación desde n=2 hasta n=100
    ani = FuncAnimation(fig, update, frames=range(2, 101), blit=True)
    
    # Guardamos la animación como GIF a 10 cuadros por segundo
    ani.save('seno_interpolacion.gif', writer='pillow', fps=10)
    print("¡Éxito! GIF guardado como 'seno_interpolacion.gif'")

if __name__ == "__main__":
    generar_gif()