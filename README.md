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
* [Github pages apex domain setup guide](https://gist.github.com/sedwardsmarsh/640a66e0acec2e5c5126571112938397)
* [Verify custom domain for Github pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages)
    1. Follow steps and stop before adding a TXT DNS record with your hosting service
    2. Create the new DNS record and only use the copy-able text for your hostname:
        * your hostname should only be: *_github-pages-challenge-`<gh_username>`*
    3. Follow the remaining steps in the github tutorial
    * Thank [Derek Fong](https://derekfong.medium.com/verify-github-organizations-domain-on-namecheap-9b2af148679a) for clarifying this step
* [Get SSL certification on Github pages](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https)
* [Ashley Drake's resume page tutorial for Hugo](https://aldra.co/blog/hugo_structured_data/)
* [Hugo-coder theme configuration](https://github.com/luizdepra/hugo-coder/wiki/Configurations#complete-example)
* [More information](https://gohugo.io/getting-started/directory-structure/) about the hugo directory structure