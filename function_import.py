import wp_func

first_paragraph = " since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only fiv"

heading_tex = "Where can I get some?"

second_tex = "s 1.10.32 and 1.10.33 of ""de Finibus Bonorum et Malorum"" (The Extremes of "

full_article = wp_func.wp_p(first_paragraph)+ wp_func.wp_h2(heading_tex)+wp_func.wp_p(second_tex)

print(full_article)

