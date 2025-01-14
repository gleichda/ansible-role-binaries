# ansible-role-binaries

Installs several applications via downloading the executable and placing it in Path on Linux based systems. Only x86_64 supported! Does **not** install the package via package manager.

## Test

Run `molecule test` to test this role via docker

## Requirements

## Role Variables

See Example Playbook

## Dependencies

- ansible-role-basic

## Example Playbook

```
---
- name: Playbook
  hosts: localhost
  connection: local
  pre_tasks:
    - set_fact:
        argocdcli_version: 1.5.6
        awless_version: 0.1.11
        awscli_version: 1.18.2
        bat_version: 0.12.1
        bit_version: 0.5.8
        bottom_version: 0.6.3
        delta_version: 0.3.0
        direnv_version: 2.21.3
        dive_version: 0.10.0
        docker_compose_version: 1.25.4
        docker_version: 19.03.8
        doctl_version: 1.39.0
        dog_version: v0.1.0
        dua_version: 2.14.4
        duf_version: 0.6.0
        dust_version: 0.6.2
        dyff_version: 1.4.3
        entr_version: 4.6
        exa_version : 0.9.0
        fasd_version: 1.0.1
        fd_version: v8.1.1
        fluxctl_version: 1.19.0
        githubcli_version: 0.6.2
        gitui_version: 0.14.0
        glab_version: 1.11.1
        helm2_version: v2.16.9
        helm_version: 3.1.1
        istioctl_version: 1.5.1
        jq_version: 1.6
        k6_version: v0.29.0
        k9s_version: 0.19.1
        kind_version: 0.7.0
        kops_version: 1.16.0
        kube_linter_version: 0.2.2
        kubectl_version: 1.18.0
        kubectx_version: v0.9.1
        kubectx_version: v0.9.1
        kubens_version: v0.9.1
        kubens_version: v0.9.1
        kubeseal_version: 0.12.4
        kubeval_version: 0.15.0
        kustomize_version: 3.5.5
        lazygit_version: 0.20.4
        lf_version: r21
        mdbook_version: 0.3.7
        nnn_version: 3.3
        pet_version: 0.3.6
        polaris_version: 1.2.1
        popeye_version: 0.7.1
        ripgrep_version: 12.1.1
        scc_version: 3.0.0
        sd_version: 0.7.6
        slack_term_version: 0.5.0
        stern_version: 1.11.0
        tflint_version: v0.21.0
        tfswitch_version: 0.8.832
        tokei_version: 12.1.2
        xsv_version: 0.13.0
        yq_version: 3.3.2
        zoxide_version: 0.7.3
  roles:
    - ansible-role-binaries
```

## License

MIT
