---
title: Bombay Favourites
author: Karen
---

{% for bcat in site.bombay_categories %}
   <section class='section' id="bcat[1]">
      <h2 class="title"> {{ bcat[1] }} </h2>
         <div class='grid'>
            {% for recipe in site.recipes %}
               {% if recipe.section == 'bombay' and recipe.category == bcat[0] %}
                  <div class="cell">
                     <a href="{{ recipe.url }}"> {{ recipe.title }}</a>
                  </div>
               {% endif %}
            {% endfor %}
         </div>
   </section>
{% endfor %}
