"""Calculo del area y el precio de una lamina de marmol.

Programa de ejemplo para el ejercicio de versionamiento con Git.
Evidencia GA7-220501096-AA1-EV05 - SENA ADSO ficha 3235867.
"""

PRECIO_METRO_CUADRADO = 185_000  # pesos colombianos por metro cuadrado


def calcular_area(largo_cm: float, ancho_cm: float) -> float:
    """Devuelve el area de la lamina en metros cuadrados."""
    if largo_cm <= 0 or ancho_cm <= 0:
        raise ValueError("Las dimensiones deben ser mayores que cero.")
    return (largo_cm / 100) * (ancho_cm / 100)


def calcular_precio(area_m2: float, precio_m2: float = PRECIO_METRO_CUADRADO) -> float:
    """Devuelve el precio de la lamina segun su area."""
    return area_m2 * precio_m2


def main() -> None:
    largo = float(input("Largo de la lamina en cm: "))
    ancho = float(input("Ancho de la lamina en cm: "))
    area = calcular_area(largo, ancho)
    precio = calcular_precio(area)
    print(f"Area: {area:.2f} m2")
    print(f"Precio estimado: $ {precio:,.0f} COP")


if __name__ == "__main__":
    main()
