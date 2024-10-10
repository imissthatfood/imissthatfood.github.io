---
layout: default
title: My cakes
---

<div class='grid'>
   {% for post in site.posts %}
   <div class="cell">
      <div class="card">
         <header class="card-header">
            <p class="card-header-title">{{ post.title }}</p>
         </header>
         <div class="card-image">
            <img
               width="100%"
               src="/assets/img/{{ post.image }}"
               />
         </div>
      </div>
   </div>
   {% endfor %}
</div>
