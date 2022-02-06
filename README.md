### TODO
* `config.toml`:
    * Implement theme CSP
    * figure out hugo "Front Matter"
    * add favicons, touchIcon, 
        * [use this](https://realfavicongenerator.net) to verify functionality
    * hideColorSchemeToggle
* ~~[figure out how to get site to display properly on github](https://gohugo.io/hosting-and-deployment/hosting-on-github/)~~
* ~~[setup apex domain samedwardsmarsh.com](https://gohugo.io/hosting-and-deployment/hosting-on-github/#use-a-custom-domain) on github~~
* add twitter?

---

### Helpful Hugo resources:
* [Hugo quickstart](https://gohugo.io/getting-started/quick-start/)
* [Hosting Hugo on Github](https://gohugo.io/hosting-and-deployment/hosting-on-github/)
* [Github pages apex domain]() setup:
    1. Purchase domain from namecheap.com
    2. Login to namecheap, go to username drop down and select dashboard
    3. Go to Domain List
    4. Click manage button on your domain
    5. Click Advanced DNS tab
    6. Click add record and add two records:
        * Type: ALIAS Record | Host: @ | Target:  | TTL: Automatic
        * Type: CNAME Record | Host: www | Target: *gh_username*.github.io.
            * replace *gh_username* with your github username
    7. Add a file named CNAME that only contains *yourdomain.com*
        * for a non-apex domain, prefix *www.* to your domain inside CNAME
    8. You may need to delete the namecheap parking DNS record from your domain
    * [Big thanks](https://gist.github.com/notTag/4a60598d018124c9ac4a7b1f3e2bac9a) to this link for original guide
* [Verify custom domain for Github pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages)
    1. Follow steps and stop before adding a TXT DNS record with your hosting service
    2. Create the new DNS record and only use the copy-able text for your hostname:
        * your hostname should only be: *_github-pages-challenge-`<gh_username>`*
    3. Follow the remaining steps in the github tutorial
    * Thank [Derek Fong](https://derekfong.medium.com/verify-github-organizations-domain-on-namecheap-9b2af148679a) for clarifying this step
* [Hugo-coder theme configuration](https://github.com/luizdepra/hugo-coder/wiki/Configurations#complete-example)
* [More information](https://gohugo.io/getting-started/directory-structure/) about the hugo directory structure