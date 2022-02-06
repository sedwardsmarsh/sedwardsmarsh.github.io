### TODO
* `config.toml`:
    * Implement theme CSP
    * figure out hugo "Front Matter"
    * add favicons, touchIcon, hideColorSchemeToggle
* ~~[figure out how to get site to display properly on github](https://gohugo.io/hosting-and-deployment/hosting-on-github/)~~
* ~~[setup apex domain samedwardsmarsh.com](https://gohugo.io/hosting-and-deployment/hosting-on-github/#use-a-custom-domain) on github~~
* add twitter?

---

### Helpful Hugo resources:
* [Hugo quickstart](https://gohugo.io/getting-started/quick-start/)
* [Hosting Hugo on Github](https://gohugo.io/hosting-and-deployment/hosting-on-github/)
* Instructions for setting up an apex domain with Hugo and Github pages:
    1. Purchase domain from namecheap.com
    2. Login to namecheap, go to username drop down and select dashboard
    3. Go to DomainList
    4. Click manage button
    5. Click Advanced DNS tab
    6. Click add record and add two records:
        * Type: ALIAS Record | Host: @ | Target:  | TTL: Automatic
        * Type: CNAME Record | Host: www | Target: *gh_un*.github.io.
            * replace *gh_un* with your github username
    7. Add a file named CNAME that only contains *yourdomain.com*
        * for a non-apex domain, prefix *www.* to your domain inside CNAME
* [Hugo coder theme configuration](https://github.com/luizdepra/hugo-coder/wiki/Configurations#complete-example)
* [More information](https://gohugo.io/getting-started/directory-structure/) about the hugo directory structure