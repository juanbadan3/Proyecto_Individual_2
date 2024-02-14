# Homicidios por siniestros viales en la Ciudad Autónoma de Buenos Aires, Argentina

![Siniestros](https://www.agenciapi.co/sites/default/files/inline-images/image_content_35944286_20200625180959.jpg)

## Introducción

Este proyecto nos sumerge en el rol de un Analista de Datos en el equipo de analistas de una firma consultora. La solicitud proviene del **Observatorio de Movilidad y Seguridad Vial (OMSV)**, un centro de estudios que depende de la Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires (CABA).
El objetivo es generar un análisis de datos sobre homicidios en siniestros viales ocurridos en CABA entre 2016 y 2021 para proporcionar información crucial que guíe la toma de decisiones y la implementación de medidas para reducir las víctimas fatales en accidentes de tráfico.

## Problematica

Los siniestros viales representan eventos críticos en las vías públicas, caracterizados por la colisión o interacción entre vehículos, peatones u objetos fijos. Estos incidentes abarcan una amplia gama de situaciones, desde choques de automóviles y motocicletas hasta atropellos y caídas de vehículos.

En el contexto de la Ciudad Autónoma de Buenos Aires (CABA), este fenómeno adquiere una relevancia significativa debido al alto volumen de tráfico y la densidad poblacional. Con una población de 3,121,707 habitantes distribuidos en una superficie de 200 $km^2$ ([Fuente](https://www.argentina.gob.ar/caba#:~:text=Poblaci%C3%B3n%3A%203.120.612%20habitantes%20(Censo%202022).))., y un parque automotor que alcanza los 1,616,327 vehículos ([Fuente](https://www.estadisticaciudad.gob.ar/eyc/?p=41995))., los siniestros viales se convierten en una preocupación central.

Estos incidentes no solo generan impactos en términos de daños materiales, sino que también pueden tener consecuencias graves o fatales para los involucrados. La seguridad de los residentes, visitantes y la integridad de la infraestructura vial se ven comprometidas, lo que subraya la importancia de abordar este problema de manera integral.

La prevención de siniestros viales se erige como una prioridad clave, y la implementación de políticas efectivas se vuelve esencial para garantizar la seguridad en las calles de la ciudad. La concientización, la regulación del tráfico y medidas de seguridad vial son herramientas fundamentales para mitigar los riesgos asociados con estos eventos y fomentar un entorno urbano más seguro para todos.


## Datos

Para este proyecto se trabajó con la **Bases de Víctimas Fatales en Siniestros Viales** que se encuentra en formato de Excel y contiene dos pestañas de datos:

* **HECHOS**: que contiene una fila de hecho con id único y las variables temporales, espaciales y participantes asociadas al mismo.
* **VICTIMAS**: contiene una fila por cada víctima de los hechos y las variables edad, sexo y modo de desplazamiento asociadas a cada víctima. Se vincula a los HECHOS mediante el id del hecho.

En este [link](https://data.buenosaires.gob.ar/dataset/victimas-siniestros-viales) se encuentran los datos utilizados en el análisis.

## Tecnologías utilizadas

Para la realización del proyecto de Extracción, Transformación y Carga (ETL), Análisis Exploratorio de Datos (EDA), así como el desarrollo del dashboard se emplearon diversas tecnologías y herramientas para llevar a cabo cada fase del proyecto de manera efectiva. A continuación, se detallan las tecnologías utilizadas:

**ETL (Extracción, Transformación y Carga) con Python y Pandas**:

**Python**: Se utilizó el lenguaje de programación Python debido a su versatilidad y amplia gama de bibliotecas, especialmente Pandas, que es una herramienta poderosa para manipulación y análisis de datos.
**Pandas**: Esta biblioteca de Python fue esencial para realizar las operaciones de ETL, incluyendo la limpieza, transformación y manipulación de los datos.
**Análisis Exploratorio de Datos (EDA)** con Python y Pandas:

**Python y Jupyter Notebooks**: Se emplearon Jupyter Notebooks como entorno de desarrollo interactivo para realizar el análisis exploratorio de datos en Python.
**Pandas, Matplotlib y Seaborn**: Estas bibliotecas de Python fueron utilizadas para visualizar y analizar datos, generando gráficos y estadísticas descriptivas.
**Desarrollo de Dashboard** con Power BI:

**Power BI**: Se eligió Power BI como herramienta para la creación del dashboard interactivo debido a su capacidad para conectar y visualizar datos de manera efectiva. Power BI permite la integración de múltiples fuentes de datos y ofrece una variedad de opciones de visualización.
**DAX (Data Analysis Expressions)**: En Power BI, se emplearon expresiones DAX para realizar cálculos personalizados y definir medidas específicas para el análisis de datos.
**En resumen**, el proyecto se ejecutó con un enfoque integral utilizando Python y Pandas para las fases de ETL y EDA, mientras que Power BI se seleccionó como la herramienta principal para la creación del dashboard interactivo, aprovechando sus capacidades de visualización y análisis de datos. Este enfoque combinado proporcionó una solución robusta y efectiva para la exploración y presentación de la información contenida en el conjunto de datos.

para encontrar el dashboard click [aquí](https://github.com/juanbadan3/Proyecto_Individual_2/blob/main/PI_02_DA.pbix).
 
## ETL y EDA

En primer lugar, se realizó un proceso de extracción, transformación y carga de los datos (ETL), tanto de "HECHOS" como "VÍCTIMAS", donde se estandarizaron nombres de las variables, se analizaron nulos y duplicados de los registros, se eliminaron columnas redundantes o con muchos valores faltantes, entre otras tareas. Una vez finalizado este proceso para los dos conjuntos de datos de "Homicidios" se procedió a unir los dos conjuntos en uno solo denominado `df_homicidios`.

En segundo lugar, se procedió a realizar un análisis exploratorio exahustivo (EDA), con la finalidad de encontrar patrones que permitan generar información que le permita a las autoridades locales tomar medidas para disminuir la cantidad de víctimas fatales de los siniestros viales. Todos los detalles de este análisis se encuentran [aquí](https://github.com/juanbadan3/Proyecto_Individual_2/blob/main/PO_02_DA%20EDA.ipynb).

## Análisis de los Datos

Se inició el análisis exploratorio de la variable temporal para comprender la distribución de los siniestros viales en diferentes escalas temporales. La distribución anual reveló que alrededor del 60% de las víctimas fatales se registraron en los primeros 3 años del conjunto de datos, con una disminución notable en el año 2020 debido a las medidas de cuarentena por COVID-19. A lo largo del año, se observa una variación mensual marcada, con un pico de víctimas en diciembre. No obstante, esta tendencia no es tan evidente entre los distintos años, siendo este resultado influido por la flexibilización de las medidas de cuarentena.

Descendiendo en la escala temporal, se constató que el 70% de las víctimas perdieron la vida entre lunes y viernes, sugiriendo una posible relación con el traslado diario al trabajo. Sin embargo, en la distribución semanal, no se observaron diferencias significativas entre los distintos días, indicando que la cantidad de víctimas en un sábado o domingo es aproximadamente la misma para todo el conjunto de datos.

Al analizar las franjas horarias, se identificó que el 12% de las víctimas registró el mayor número de incidentes entre las 6 y las 8 de la mañana, sugiriendo una posible conexión con el horario de ingreso al trabajo. No obstante, al profundizar en esta franja horaria, se observó que el 55% de estas víctimas estuvo involucrado en hechos ocurridos durante el fin de semana.

Posteriormente, se exploró el perfil de la víctima, destacando que el 77% de las víctimas son de género masculino. Casi el 50% de ellas se encuentran en un rango etario de 26 a 35 años, y el 84% de este grupo pertenece al género masculino.

Al analizar el rol de la víctima en el momento del hecho, se encontró que el 48% era conductor, distribuyéndose principalmente en un 77% de víctimas que se movilizaban en moto y un 19% en auto. En cuanto al medio de transporte al momento del hecho, el 42% de las víctimas son conductores de moto, siendo el 88% de estos conductores de género masculino.

Finalmente, se buscaron patrones en la distribución espacial de los siniestros, resaltando que en todas las comunas de CABA es común que los accidentes ocurran en avenidas, vías anchas de al menos 13 metros. El 62% de las víctimas perdió la vida en avenidas, siendo el 82% de estos casos en el cruce de avenidas con otras calles. Este comportamiento se mantuvo consistente a lo largo de los años, variando el rol de la víctima entre moto y peatón en diferentes comunas.
## KPI

En función de lo analizado en el punto anterior, se plantearon dos objetivos en relación a la disminución de la cantidad de víctimas fatales de los siniestros viales, desde los cuales se proponen dos indicadores de rendimiento clave o KPI.

* *Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses, en CABA, en comparación con la tasa de homicidios en siniestros viales del semestre anterior*

  La tasa de homicidios en siniestros viales se define como **Tasa de homicidios en siniestros viales** ael número de víctimas fatales en accidentes de tránsito por cada 100,000 habitantes durante un período específico, en este caso, 6 meses. La fórmula es:

    $\text{Tasa de homicidios en siniestros viales} = \frac{\text{Número de homicidios en siniestros viales}}{\text{Población total}}·100,000$

    Utilizando datos poblacionales (censo) de 2010, 2022 y el censo de 2021, se calculó que la tasa para el primer semestre de 2021 fue de 1.77. El objetivo propuesto es reducir esta tasa en un 10%, alcanzando un valor de 1.60. El KPI para este período fue de 1.35, lo que indica que se cumplió con el objetivo.

    
* *Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año, en CABA, respecto al año anterior*

    Dado que el 42% de las víctimas mortales viajaban en moto, se propone monitorear la cantidad de accidentes mortales de motociclistas. La fórmula para medir la evolución es:

    $\text{Cantidad de accidentes mortales de motociclistas} = -\frac{\text{Víctimas moto año anterior - Víctimas moto año actual}}{\text{Víctimas moto año anterior}}·100$

    Donde:
    - $\text{Víctimas moto año anterior}$: Número de accidentes mortales con víctimas en moto en el año anterior
    - $\text{Víctimas moto año actual}$: Número de accidentes mortales con víctimas en moto en el año actual 

    Se toma el año 2021 como el actual y el 2020 como el anterior. La cantidad para el año 2020 fue de -44.00. El objetivo es una reducción del 7%, alcanzando -40.92. Sin embargo, el resultado para el año 2021 fue de 64.29, lo que indica un aumento del 64% en la cantidad de muertes de motociclistas con respecto al 2020.

* *A continuación podemos ver los gráficos de los KPIs:*

[aquí](https://github.com/juanbadan3/Proyecto_Individual_2).
  
  
  
## Conclusiones y recomendaciones

Entre los años 2016 a 2021 se registraron 717 víctimas fatales en accidentes de tránsito. El 70% de las víctimas se registraron durante la semana. En cuanto a la franja horaria, el 12% de los hechos ocurre entre las 6 y las 8 de la mañana, pero durante los fines de semana. Diciembre es el mes que resulta con el máximo de fallecimientos en el período analizado.

El 77% de las víctimas fatales fueron de sexo masculino, de los cuales casi el 50% tenía entre 25 y 44 años de edad. En relación al tipo de usuario, el 42% fueron motociclistas. El 62% de los homicidios ocurrió en algún punto de las avenidas de CABA, siendo el 82% de ellos en un cruce de la autopista con alguna otra calle. En ese sentido, el 75% de los hechos ocurrieron en cruces de calles.

Finalmente, para el segundo semestre del año 2021, se cumplió con el objetivo de bajar la tasa de homicidios en siniestros viales, pero no se cumplieron los objetivos de reducir la cantidad de accidentes mortales en motociclistas ni en avenidas para el año 2021 respecto del año 2020.

En función de lo anterior, se hacen las siguientes recomendaciones:

* Continuar monitoreando los objetivos propuestos acompañados de campañas puntuales, en especial a conductores de motos y usuarios de las avenidas.
* Reforzar las campañas de seguridad vial entre los días viernes a lunes, intensificando particularmente en el mes de Diciembre.
* Puntualizar campañas de conducción segura en avenidas y cruces de calles.
* Dirigir las campañas de seguridad hacia el sexo masculino, especialmente en cuanto a conducción en moto.



Se registraron 717 víctimas fatales en accidentes de tránsito entre los años 2016 y 2021, siendo el 70% de estas víctimas eventos ocurridos durante la semana. En cuanto a la franja horaria, el 12% de los incidentes se desarrolla entre las 6 y las 8 de la mañana, pero exclusivamente durante los fines de semana. Diciembre destaca como el mes con el mayor número de fallecimientos en el periodo analizado.

El 77% de las víctimas fatales fueron hombres, y casi el 50% de ellos se encontraba en el rango de edad de 25 a 44 años. En cuanto al tipo de usuario, el 42% fueron motociclistas. Además, el 62% de los homicidios ocurrió en alguna avenida de CABA, siendo el 82% de estos en un cruce de la autopista con alguna otra calle. En este contexto, el 75% de los eventos tuvieron lugar en cruces de calles.

Para el segundo semestre del año 2021, se logró el objetivo de reducir la tasa de homicidios en siniestros viales, pero no se cumplieron las metas de disminuir la cantidad de accidentes mortales en motociclistas ni en avenidas para el año 2021 en comparación con el año 2020.

Analizando de forma exaustiva los resultados antes expuestos, se se hacen las siguientes recomendaciones.


1. **Implementar Programas de Educación Vial:**
   - Desarrollar programas educativos destinados a la población en general, con énfasis en conductores jóvenes, para aumentar la conciencia sobre la importancia de la seguridad vial.
   - Colaborar con instituciones educativas para incluir contenidos de seguridad vial en los programas de estudio.

2. **Fomentar el Uso de Equipamiento de Seguridad:**
   - Promover campañas de concientización sobre la importancia del uso de cascos, cinturones de seguridad y otros elementos de protección.
   - Colaborar con autoridades locales para garantizar la aplicación y el cumplimiento de normativas relacionadas con el equipamiento de seguridad.

3. **Mejorar la Señalización Vial:**
   - Evaluar y mejorar la señalización en áreas críticas y cruces de calles para reducir la posibilidad de accidentes.
   - Utilizar tecnologías innovadoras, como señalización inteligente, para mejorar la visibilidad y comprensión de las indicaciones viales.

4. **Promover Alternativas de Transporte:**
   - Incentivar el uso de medios de transporte alternativos, como bicicletas y transporte público, para reducir la congestión vial y la frecuencia de accidentes.
   - Desarrollar infraestructuras amigables con modos de transporte no motorizados.

5. **Monitoreo Continuo y Análisis de Datos:**
   - Establecer un sistema de monitoreo constante de datos de accidentes para identificar tendencias y áreas de riesgo.
   - Utilizar análisis predictivos para anticipar posibles aumentos en la frecuencia de accidentes y tomar medidas preventivas.

6. **Colaborar con Empresas y Comunidades:**
   - Trabajar en colaboración con empresas para implementar políticas internas de seguridad vial y fomentar prácticas seguras entre los empleados.
   - Involucrar a la comunidad en programas de seguridad vial, promoviendo la participación activa en la concientización y prevención.

7. **Evaluación Periódica de Resultados:**
   - Realizar evaluaciones periódicas de las acciones implementadas y ajustar estrategias según los resultados obtenidos.
   - Mantener una comunicación abierta con la comunidad para recoger retroalimentación y sugerencias.

Estas recomendaciones buscan abordar de manera integral la seguridad vial, involucrando a diferentes sectores de la sociedad y aplicando enfoques preventivos y educativos.


# _Autor_
- Juan David Albadan Alvarez
- E-Mail: juanalbadan3@gmail.com
- Linkedin: [Linkedin](https://www.linkedin.com/in/juan-david-albadan-689855216/)

