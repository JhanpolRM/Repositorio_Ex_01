import streamlit as st
import pandas as pd
import numpy as np
from libreria_funciones_proyecto1 import calcular_indicadores_mantenimiento
from libreria_clases_proyecto1 import EquipoMantenimiento

#CONFIGURACIÓN DE PESTAÑA DE LA APP WEB
st.set_page_config(page_title="PROYECTO STREAMLIT", page_icon="🐍")

#CONFIGURACIÓN DE VARIABLES
# Creamos listas vacias de variables para guardar datos mientras la app está abierta.
# session_state permite que los datos no se borren al presionar botones.

#MENU LATERAL
st.sidebar.image("Logo_dmc_institute_02.png")
st.sidebar.title("Navegación", text_alignment="center")
pagina = st.sidebar.selectbox("Seleccione una sección",["🏠 Home", "📋 Ejercicio 1", "📋 Ejercicio 2", "📋 Ejercicio 3", "📋 Ejercicio 4"])

#HOME
if pagina == "🏠 Home":
    st.title("PROYECTO 1 – APLICACIÓN EN STREAMLIT :streamlit:", text_alignment="center")
    st.image("Logo_int_Stream_Pyth.png", width="content")

    st.subheader("Módulo 1 – Python Fundamentals", text_alignment="center", divider="gray")
    st.markdown("""
    ### 📑*Descripción general del proyecto*

    Esta aplicación fue desarrollada en **Python** usando **Streamlit**. Su objetivo es demostrar
    el uso de estructuras de datos, widgets interactivos, funciones externas, clases y lógica de
    programación dentro de una interfaz web.

    La aplicación está organizada en cuatro ejercicios:

    1. **Flujo de caja con listas.**
    2. **Registro de productos con NumPy, arrays y DataFrame.**
    3. **Uso de funciones desde una librería externa.**
    4. **Uso de clases desde una librería externa con operaciones CRUD.**
    """, text_alignment="justify")
    st.markdown("---")
    st.markdown("""
    ### 💻*Tecnologías utilizadas*

    - **Python:** lenguaje principal de programación.
    - **Streamlit:** creación de la interfaz web interactiva.
    - **NumPy:** manejo de arreglos y operaciones numéricas.
    - **Pandas:** creación y visualización de tablas tipo DataFrame.
    - **Librerías externas:** uso de archivos `.py` con funciones y clases.
    """, text_alignment="justify")
    st.markdown("---")
    st.markdown("""
    ### 👨‍🔧*Elaborado por*
    **Jhanpol Rosales Muñoz**\n 
    Bachiller en Ingeniería Mecánica.
    """)
    st.markdown("---")
    st.subheader("*2026*", text_alignment="center")

#EJERCICIO 01
#
if "movimientos" not in st.session_state:
    st.session_state.movimientos = []
#
elif pagina == "📋 Ejercicio 1":
    st.title("Ejercicio 1 – Flujo de caja con listas", text_alignment="center")

    st.markdown("""
    En este ejercicio se registran movimientos financieros. 
    Cada movimiento contiene un concepto, un tipo de movimiento y un valor.
    
    El programa calcula:
    
    - Total de ingresos.
    - Total de gastos.
    - Saldo final.
    - Estado del flujo de caja.
    """, text_alignment="justify")

    st.subheader("Registrar movimiento financiero")
    concepto=st.text_input("Ingrese el concepto del movimiento", placeholder="Ejemplo: Venta, Compra, Pago")
    tipo_movimiento=st.selectbox("Tipo de Movimiento", ["Ingreso", "Gasto"])
    valor=st.number_input("Valor del movimiento", min_value=0, step=5)

    if st.button("Agregar Movimiento"):
        if concepto.strip()=="":
            st.warning("Debes agregar un concepto antes de agregar el movimiento")
        elif valor<=0:
            st.warning("El valor debe ser mayor a cero")
        else:
            movimiento={
                "Concepto":concepto,
                "Tipo":tipo_movimiento,
                "Valor":valor
            }
            st.session_state.movimientos.append(movimiento)
            st.success("✅ Movimiento agregado correctamente.")

    if st.button("Limpiar movimiento"):
        st.session_state.movimientos = []
        st.info("La lista de movimientos fue limpiada")

    st.subheader("Movimientos Registrados")

    if len(st.session_state.movimientos)>0:
        tabla_movimientos = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(tabla_movimientos)
        total_ingresos=tabla_movimientos[tabla_movimientos["Tipo"]=="Ingreso"]["Valor"].sum()
        total_gastos=tabla_movimientos[tabla_movimientos["Tipo"]=="Gasto"]["Valor"].sum()
        saldo_final=total_ingresos-total_gastos

        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Total de ingresos",f"S/{total_ingresos:.2f}")
        with col_b:
            st.metric("Total de gastos",f"S/{total_gastos:.2f}")
        with col_c:
            st.metric("Saldo Final",f"S/{saldo_final:.2f}")

        if saldo_final>0:
            st.success("El flujo de caja está a favor.")
        else:
            st.error("El flujo de caja está en contra.")
    else:
        st.info("Todavía no se han registrado movimientos.")


    with st.expander("Ver explicación del ejercicio"):
        st.write("""
        En este ejercicio se puede apreciar que los movimientos se almacenan en una lista llamada `movimientos`. 
        Cada movimiento se guarda como un diccionario con tres datos: concepto, tipo y valor. 
        Luego se usa un DataFrame para mostrar la información en forma de tabla.
        """)

#EJERCICIO 02
#
if "productos" not in st.session_state:
    st.session_state.productos = []
#
elif pagina=="📋 Ejercicio 2":
   st.title("Ejercicio 2 – Registro con NumPy, arrays y DataFrame", text_alignment= "center")

   st.markdown("""
    En este ejercicio se registran productos usando widgets de Streamlit.
    Los datos ingresados se convierten en **arrays de NumPy** y luego se muestran en un
    **DataFrame**.

    Cada registro contiene:

    - Nombre del producto.
    - Categoría.
    - Precio.
    - Cantidad.
    - Total.
    """, text_alignment="justify")

   st.subheader("Registro de productos")

   nombre_producto=st.text_input("Nombre del producto", placeholder="Ejemplo: Laptop, Aromatizante, Fruta, etc")
   categoria=st.selectbox("Categoría", ["Tecnología", "Alimentos", "Limpieza", "Otros"])
   precio=st.number_input("Precio", min_value=0.0, step=1.0)
   cantidad=st.number_input("Cantidad", min_value=0, step=1)

   if st.button("Agregar producto"):
        if nombre_producto.strip() == "":
            st.warning("Debes ingresar el nombre del producto")
        elif precio<= 0:
            st.warning("El precio debe ser mayor que cero")
        elif cantidad<=0:
            st.warning("El cantidad debe ser mayor que cero")
        else:
            producto={
                "Producto": nombre_producto,
                "Categoria": categoria,
                "Precio": precio,
                "Cantidad": cantidad
            }
            st.session_state.productos.append(producto)
            st.success("✅ Producto agregado correctamente")

   if st.button("Limpiar producto"):
        st.session_state.productos = []
        st.info("La tabla de productos fue limpiada")

   st.subheader("Tabla actualizada de productos")

   if len(st.session_state.productos)>0:
       tabla_productos = pd.DataFrame(st.session_state.productos)

       productos_array= np.array(tabla_productos["Producto"])
       categorias_array= np.array(tabla_productos["Categoria"])
       precios_array= np.array(tabla_productos["Precio"])
       cantidades_array= np.array(tabla_productos["Cantidad"])
       totales_array=precios_array * cantidades_array

       tabla_numpy=pd.DataFrame({
           "Producto": productos_array,
           "Categoria": categorias_array,
           "Precio": precios_array,
           "Cantidad": cantidades_array,
           "Total": totales_array
       })

       st.dataframe(tabla_numpy)

       col_a, col_b, col_c = st.columns(3)
       with col_a:
           st.metric("Registros", len(tabla_numpy))
       with col_b:
           st.metric("Total general", f"S/ {np.sum(totales_array):.2f}")
       with col_c:
           st.metric("Promedio por registro", f"S/ {np.mean(totales_array):.2f}")
   else:
       st.info("Todavía no se han registrado productos.")

   with st.expander("Ver explicación del ejercicio"):
       st.write("""
       Primero se registran los productos mediante widgets. Luego, la información se transforma
       en arrays de NumPy. El total de cada producto se calcula de forma vectorizada usando
       `totales = precios * cantidades`. Finalmente, los resultados se muestran en un DataFrame.
       """)

#EJERCICIO 03
#
if "historial_funciones" not in st.session_state:
    st.session_state.historial_funciones = []

#
elif pagina == "📋 Ejercicio 3":
    st.title("Ejercicio 3 - Uso de funciones desde una librería externa", text_alignment="center")

    st.markdown("""
    En este ejercicio se utiliza una función externa, importada desde una libreria de funciones externa proveniente del archivo
    `libreria_funciones_proyecto1.py`.

    La función seleccionada está relacionada con el mantenimiento industrial y permite calcular:

    - MTBF (Mean Time Between Failures /tiempo medio entre fallos).
    - MTTR (Mean Time To Repair /tiempo medio de reparación).
    - Disponibilidad.
    """, text_alignment="justify")

    funcion_seleccionada= st.selectbox("Seleccione la función", ["calcular_indicadores_mantenimiento"])

    st.subheader("Ingreso de parámetros")

    nombre_equipo= st.text_input("Nombre de equipo", placeholder="Bomba Centrífuga, Ventilador Axial, Etc")
    tiempo_operacion= st.number_input("Tiempo de operación (h)", min_value=0.0, value= 7.0, step=1.0)
    numero_fallas= st.number_input("Numero de fallas", min_value=1, value= 1, step=1)
    tiempo_reparacion= st.number_input("Tiempo total de reparación (h)", min_value=0.1, value=10.0, step=1.0)

    if st.button("Ejecutar función"):
        try:
            resultado=calcular_indicadores_mantenimiento(
                tiempo_operacion,
                numero_fallas,
                tiempo_reparacion
            )
            registro={"Equipo": nombre_equipo,
                      "Tiempo de operación (h)": tiempo_operacion,
                      "Numero fallas": numero_fallas,
                      "Tiempo de reparación (h)": tiempo_reparacion,
                      "MTBF (h)": resultado["mtbf_h"],
                      "MTTR (h)": resultado["mttr_h"],
                      "Disponibilidad (%)": resultado["disponibilidad_pct"]
            }

            st.session_state.historial_funciones.append(registro)
            st.success("✅ Función ejecutada correctamente")

            st.subheader("Resultado Obtenido")
            st.write(resultado)

        except Exception as error:
            st.error(f"❌ Ocurrió un error: {error}")

    st.subheader("Historial de Resultados")

    if len(st.session_state.historial_funciones)>0:
        historial= pd.DataFrame(st.session_state.historial_funciones)
        st.dataframe(historial)
    else:
        st.info("Todavía no existen resultados guardados.")

    if st.button("Limpiar historial"):
        st.session_state.historial_funciones = []
        st.info("El historial fue limpiado")

    with st.expander("Ver explicación del ejercicio"):
        st.write("""
        Este ejercicio demuestra cómo importar y usar una función creada en otro archivo Python.
        La función recibe parámetros ingresados mediante widgets, calcula indicadores de
        mantenimiento y devuelve un diccionario con los resultados.
        """)

#EJERCICIO 04
#
if "equipos" not in st.session_state:
    st.session_state.equipos = []

#
elif pagina=="📋 Ejercicio 4":
    st.title("Ejercicio 4 - Uso de clases desde una librería externa con 📊 CRUD", text_alignment="center")

    st.markdown("""
        En este ejercicio se utiliza la clase `EquipoMantenimiento` la cual es importada desde el archivo externo
        `libreria_clases_proyecto1.py`.

        Se implementan operaciones básicas tipo **CRUD**:

        - **Crear:** registrar equipos.
        - **Leer:** visualizar equipos registrados.
        - **Actualizar:** modificar datos de un equipo.
        - **Eliminar:** borrar equipos registrados.
        """, text_alignment="justify")

    # Menú de navegación de CRUD
    opcion = st.sidebar.selectbox("Selecciona una actividad",
                                  ["Crear Nuevo Registro", "Leer Registro", "Actualizar Registro", "Eliminar Registro"])
    #Crear nuevo registro de Equipo
    if opcion=="Crear Nuevo Registro":
        st.subheader("➕ Crear Nuevo Registro de Equipo")

        nombre_equipo = st.text_input("Nombre del equipo:", placeholder="Bomba Centrífuga, Ventilador Axial, Compresor de aire, etc")
        horas_operacion = st.number_input("Horas de operación:", min_value=0.01, value=1000.0, step=10.0)
        numero_fallas_equipo = st.number_input("Número de fallas:", min_value=1, value=5, step=1, key="crear_fallas")
        horas_reparacion = st.number_input("Horas de reparación:", min_value=0.0, value=20.0, step=1.0)

        if st.button("Crear Registro"):
            try:
                equipo = EquipoMantenimiento(
                    nombre_equipo=nombre_equipo,
                    horas_operacion=horas_operacion,
                    numero_fallas=numero_fallas_equipo,
                    horas_reparacion=horas_reparacion
                )
                resumen = equipo.resumen()
                registro_equipo = {
                    "Nombre": nombre_equipo,
                    "Horas operación": horas_operacion,
                    "Número fallas": numero_fallas_equipo,
                    "Horas reparación": horas_reparacion,
                    "MTBF (h)": resumen["mtbf_h"],
                    "MTTR (h)": resumen["mttr_h"],
                    "Disponibilidad (%)": resumen["disponibilidad_pct"]
                }
                st.session_state.equipos.append(registro_equipo)
                st.success("✅ Equipo Registrado Correctamente.")

            except Exception as error:
                st.error(f"❌ Ocurrió un error: {error}")

    # Leer registro creado del Equipo
    elif opcion == "Leer Registro":
        st.subheader("📋 Leer Registro")

        if len(st.session_state.equipos)>0:
            df_equipos = pd.DataFrame(st.session_state.equipos)
            st.dataframe(df_equipos)
            disponibilidad_promedio = df_equipos["Disponibilidad (%)"].mean()
            st.metric("Disponibilidad promedio", f"{disponibilidad_promedio:.2f} %")
        else:
            st.info("Todavía no existen equipos registrados.")

    # Actualizar registro del Equipo
    elif opcion == "Actualizar Registro":
        st.subheader("🔄 Actualizar Registro")

        if len(st.session_state.equipos)>0:
            indice_actualizar = st.selectbox(
                "Selecciona el equipo a actualizar:",
                range(len(st.session_state.equipos)),
                format_func=lambda i: st.session_state.equipos[i]["Nombre"]
            )
            equipo_actual = st.session_state.equipos[indice_actualizar]

            nuevo_nombre = st.text_input("Nuevo nombre:", value=equipo_actual["Nombre"])
            nuevas_horas_operacion = st.number_input(
                "Nuevas horas de operación:",
                min_value=0.01,
                value=float(equipo_actual["Horas operación"]),
                step=10.0
            )
            nuevo_numero_fallas = st.number_input(
                "Nuevo número de fallas:",
                min_value=1,
                value=int(equipo_actual["Número fallas"]),
                step=1,
                key="actualizar_fallas"
            )
            nuevas_horas_reparacion = st.number_input(
                "Nuevas horas de reparación:",
                min_value=0.0,
                value=float(equipo_actual["Horas reparación"]),
                step=1.0
            )

            if st.button("Actualizar Registro"):
                try:
                    equipo = EquipoMantenimiento(
                        nombre_equipo=nuevo_nombre,
                        horas_operacion=nuevas_horas_operacion,
                        numero_fallas=nuevo_numero_fallas,
                        horas_reparacion=nuevas_horas_reparacion
                    )
                    resumen = equipo.resumen()
                    st.session_state.equipos[indice_actualizar] = {
                        "Nombre": nuevo_nombre,
                        "Horas operación": nuevas_horas_operacion,
                        "Número fallas": nuevo_numero_fallas,
                        "Horas reparación": nuevas_horas_reparacion,
                        "MTBF (h)": resumen["mtbf_h"],
                        "MTTR (h)": resumen["mttr_h"],
                        "Disponibilidad (%)": resumen["disponibilidad_pct"]
                    }

                    st.success("✅ Registro Actualizado Correctamente")

                except Exception as error:
                    st.error(f"❌ Ocurrió un eror: {error}")
        else:
            st.info("No hay registros para actualizar.")

    # Eliminar registro del Equipo
    elif opcion == "Eliminar Registro":
        st.subheader("🗑️ Eliminar Registro")

        if len(st.session_state.equipos)>0:
            indice_eliminar = st.selectbox(
                "Selecciona el equipo a eliminar:",
                range(len(st.session_state.equipos)),
                format_func=lambda i: st.session_state.equipos[i]["Nombre"],
                key="selector_eliminar"
            )
            st.warning(f"⚠️ Esta acción eliminará el registro seleccionado")

            if st.button("Eliminar registro"):
                equipo_eliminado = st.session_state.equipos.pop(indice_eliminar)
                st.success(f"☑️ Se eliminó el equipo: {equipo_eliminado['Nombre']}.")
        else:
            st.info("No hay registros para eliminar.")

    with st.expander("Ver explicación del ejercicio"):
        st.write("""
        Este ejercicio usa programación orientada a objetos mediante la clase `EquipoMantenimiento`.
        Cada vez que se crea o actualiza un registro, se instancia un objeto de la clase y se usan
        sus métodos para calcular MTBF, MTTR y disponibilidad. Los datos se guardan en
        `st.session_state.equipos` para permitir las operaciones CRUD dentro de la aplicación.
        """)
























