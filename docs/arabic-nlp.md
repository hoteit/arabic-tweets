---
layout: page
title: Arabic NLP Resources 
permalink: /nlp/
---

{% for nlp_link in site.arabic_nlp %}
  <h3>
    <a href="{{ nlp_link.url }}">{{ nlp_link.title }}</a>
  </h3>
  <p>{{ nlp_link.content | markdownify }}(source <a href="{{ nlp_link.url }}">{{ nlp_link.source}}</a>)</p>
{% endfor %}