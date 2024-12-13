---
layout: page
title: CV
permalink: /cv/
---
<h1>{{ site.data.cv.name }}</h1>
<p><strong>{{ site.data.cv.title }}</strong></p>

<h2>Contact</h2>
<ul>
  <li>Email: <a href="mailto:{{ site.data.cv.contact.email }}">{{ site.data.cv.contact.email }}</a></li>
  <li>Phone: {{ site.data.cv.contact.phone }}</li>
  <li>LinkedIn: <a href="{{ site.data.cv.contact.linkedin }}" target="_blank">LinkedIn Profile</a></li>
  <li>GitHub: <a href="{{ site.data.cv.contact.github }}" target="_blank">GitHub Profile</a></li>
</ul>
{% for section in site.data.cv.sections %}
  <h2>{{ section.title }}</h2>
  <ul>
    {% for item in section.items %}
        {% if item.skill %}
          <strong>{{ item.category }}:</strong> {{ item.name }}<br/>
        {% elsif item.position %}
          <strong>{{ item.position }}</strong><br/>
          <em>{{ item.institution }} ({{ item.dates }})</em><br/>
          <p>{{ item.description }}</p>
        {% elsif item.degree %}
          <strong>{{ item.degree }}</strong><br/>
          <em>{{ item.institution }} ({{ item.dates }})</em><br/>
          <p>{{ item.description }}</p>
        {% endif %}
    {% endfor %}
  </ul>
{% endfor %}


