---
layout: default
title: My cakes
---

<div class='grid'>
   {% for post in site.posts %}
   <div class="cell">
      <div class="card">
         <header class="card-header">
            <a href="{{post.url}}"><p class="card-header-title">{{ post.title }}</p></a>
         </header>
         <div class="card-image">
            <img
               width="100%"
               src="/assets/img/{{ post.image }}"
               />
         </div>
	<footer class="card-footer">
{% for tag in post.tags %}
         <div class="tag">
           <span class="tag-text">
             <a href="#">{{ tag }}</a>
           </span>
         </div>
{% endfor %}
</footer>
      </div>
   </div>
   {% endfor %}
</div>
