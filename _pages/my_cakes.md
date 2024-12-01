---
layout: default
title: My cakes
---

{% for post in site.posts %}
<div class="column is-8 is-offset-2">
   <h1 class='is-title-1'>{{ post.title }}</h1>
   {{ post.date | date: "%Y" }}
   {{ post.content }}
   <br>
   <figure class="image">
      <center>
         <img src="/assets/img/{{ post.image }}"/>
      </center>
   </figure>
</div>
<div class="is-divider">
{% endfor %}
