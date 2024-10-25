from resumen.processors import procesar_articulos, generar_resumen_final


# Code for summerize the PDFs from a folder and keep the response in a folder called 'respuestas'
ruta = 'ruta/ejemplo/'
modelo = 'gpt-4o-mini'
prompt_1 = [
        {"role": "system", "content": "You are an assistant specialized in reading scientific articles and providing expert responses."},
        {"role": "user", "content": """
         I will provide you with an article. Please analyze the content and deliver a concise summary highlighting the most relevant information related to the following aspects of user requirements:

        -  Usability: How the ease of use of the system, tool, or product is described in the article.
        - Satisfaction: How user satisfaction when interacting with the system is measured or mentioned.
        - Acceptability: What factors determine whether the system or product is acceptable to users, and how this acceptance is evaluated.
        - User perspectives: Any relevant user comments, opinions, or perspectives that help understand how users experience or interact with the system or product.
        - Other relevant aspects: Any other important aspect of user requirements in the context of technology and health, such as accessibility, impact on treatment adherence, integration with other systems or technologies, or data privacy and security.

        Please provide this information clearly and concisely, highlighting only the most important details for each category.

        Text: {texto}"""}
    ]

prompt_2 = [
        {"role": "system", "content": "You are an assistant specialized in reading scientific articles and providing expert responses."},
        {"role": "user", "content": """
         I will provide you with a large text that includes summaries from many articles, each structured under the format of:

        File title: [File name]
        Text: [Summary content]

        All the summaries discuss user requirements, focusing on aspects such as usability, satisfaction, acceptability, user perspectives, and other relevant factors.

        Your task is to carefully analyze all the content and produce a synthesized response that combines the most important and relevant information across all the summaries. Ensure that your response highlights key themes and trends related to user requirements, particularly focusing on:

        Usability: Common insights or conclusions on the ease of use of the systems, tools, or products.
        Satisfaction: How user satisfaction is portrayed or measured across the various articles.
        Acceptability: Factors influencing the acceptability of the systems or tools, and how this is evaluated.
        User perspectives: Any shared or divergent user perspectives that stand out in the data.
        Other relevant factors: Any other relevant aspects mentioned, such as accessibility, treatment adherence, privacy, or technological integration.
        Summarize all this information in a clear, concise manner that captures the most critical points across the entire body of text.
         
         Summaries: {texto}
         """}
            ]
            
# Uncomment to execute the code
# procesar_articulos(ruta, modelo, prompt_1)

# File Path where the summaries are stored

ruta_2 = 'ruta/ejemplo/summaries' 

# Uncomment to execute the code
# generar_resumen_final(ruta_2, modelo, prompt_2)
    


