def wp_p(p_tex):
    code = f"<!-- wp:paragraph --><p>{p_tex}</p><!-- /wp:paragraph -->"
    return code

def wp_h2(heading_two):
    code = f"<!-- wp:heading --><h2>{heading_two}</h2><!-- /wp:heading -->"
    return code