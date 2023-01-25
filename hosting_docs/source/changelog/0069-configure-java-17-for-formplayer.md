<!--THIS FILE IS AUTOGENERATED: DO NOT EDIT-->
<!--See https://github.com/dimagi/commcare-cloud/blob/master/changelog/README.md for instructions-->
# 69. Configure Java 17 for Formplayer

**Date:** 2023-01-10

**Optional per env:** _required on all environments_


## CommCare Version Dependency
This change is not known to be dependent on any particular version of CommCare.


## Change Context
This change is to configure Java 17 for Formplayer. 

## Details
This sets a specific Java version just for formplayer. It should only affect the machine that formplayer is on and it shouldn't impact any other 
Java processes running on that machine. 

## Steps to update

1. Update commcare-cloud to the latest version
2. Add the following setting to the environment's `public.yml` and set its value accordingly:
    +++
    <pre style="background-color:#f8f8f8" class="code literal-block">
    formplayer_java_version: &#123;&#123; java_17_bin_path }}/java
    </pre>
    +++
3. Update Formplayer 
    ```
    commcare-cloud <env> ap deploy_formplayer.yml --limit=formplayer
    ```
4. Redeploy Formplayer 
    ```
    cchq <env> deploy formplayer
    ```