# Servitech — App de soporte técnico

PWA (web app instalable) para trabajo de soporte técnico en campo: **empresas, equipos, banco de tareas, repuestos e informes de servicio con firma**.

Hecha en HTML/CSS/JavaScript puro (sin frameworks ni build), con los datos guardados en el propio dispositivo (localStorage) y respaldo manual en JSON.

## Funciones

- **Portada** tipo carpeta e inicio "En servicio" con las empresas con trabajo abierto y resumen del día.
- **Empresas**: ficha editable (razón social, RUC, dirección, contacto, notas) e historial.
- **Equipos**: registrados por empresa (tipo, marca, modelo, N° de serie, ubicación).
- **Tareas**: banco con estados (Pendiente, En curso, Esperando repuestos, Completada, Cancelada), novedad, trabajo realizado y solución.
- **Repuestos / compras**: estados *Por comprar → Pedido → Recibido → Cambiado*.
- **Informes de servicio**: numeración correlativa anual, datos de la empresa, lo que se encontró, lo que se hizo, solución, repuestos usados, **firma del responsable y del técnico**, vista imprimible (PDF) y envío por WhatsApp. Al firmar, la tarea pasa a Completada.
- **Ajustes**: respaldo/restauración JSON, datos de ejemplo, nombre del técnico y moneda.

## Uso local

```bash
python -m http.server 8765 --bind 127.0.0.1
```

Abre `http://127.0.0.1:8765` en el navegador.

## Instalar en el celular (Android)

1. Abre la dirección publicada en Chrome.
2. Menú (⋮) → **Agregar a pantalla de inicio**.
3. Se abre a pantalla completa como una app y funciona sin conexión.

## Documentación del proyecto

- `modelo-de-datos-servitech.md` — modelo de datos completo (fichas y campos).
- `plantilla-servitech.xlsx` — plantilla de ejemplo de las fichas.

## Estructura

```
index.html            shell de la app (SPA)
css/app.css           estilos (tema moderno)
js/store.js           capa de datos (localStorage)
js/app.js             vistas, rutas y lógica
sw.js                 service worker (offline; solo en https)
assets/               manifest e íconos
```
