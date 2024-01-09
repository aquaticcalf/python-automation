write in markdown to generate sitemap.xml 

you can use the following fields:
- url : for urls
- lastmod : last modified date in the YYYY-MM-DD format
- changefreq : monthly/weekly/daily
- priority : on a scale of 0.1 to 1.0

example markdown : 

```md
# main
- url: https://example.xyz/
- lastmod: 2024-01-04
- changefreq: monthly
- priority: 1.0
```

corresponding xml : 

```xml
    <url>
        <loc>https://example.xyz/</loc>
        <lastmod>2024-01-04</lastmod>
        <changefreq>monthly</changefreq>
        <priority>1.0</priority>
    </url>
```

check out [example.md](example.md) and [exmaple-output-sitemap.xml](example-output-sitemap.xml) for a clear picture of what exactly u are gonna need to do and what u are getting out
