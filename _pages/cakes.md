---
layout: default
title: My cakes
---

<div class='columns'>
<div class='column'>
{% for post in site.posts %}
<h2>{{ post.title }}</h2>
<img src="/assets/img/{{ post.image }}" />
{{ post.content }}
<div class="is-divider-vertical"></div>
<hr />
{% endfor %}
</div>
</div>
