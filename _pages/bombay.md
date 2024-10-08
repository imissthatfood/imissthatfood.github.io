---
title: Bombay Favourites
author: Karen
---
<table class="table is-hoverable">
   <tbody>
      {% for bcat in site.bombay_categories %}
      <tr>
         <th>
            <a href ='{{bcat[0]}}'>{{ bcat[1] }}</a>
         </th>
         <td>
            {% for recipe in site.recipes %}
                {% if recipe.section == 'bombay' and recipe.category == bcat[0] %}
                    <i> <a href="{{ recipe.url }}">
                    {{ recipe.title }} </a></i> &middot;
                {% endif %}
            {% endfor %}
         </td>
      </tr>
      {% endfor %}
   </tbody>
</table>
