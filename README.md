# homelab-scripts

Scripts, configs, and notes from my homelab (andrelab.net). I run this stuff on a Dell T420 with Proxmox and use it to learn infrastructure and networking outside my day job as an IT specialist.

Nothing here is a polished public tool. It's a working set of things I actually use, kept in one place so I don't lose track of what I've built.

## What's in here

Automation and utilities I've written against my own stack, plus project notes I take while building things.

- **Pi-hole API scripts.** Python against the Pi-hole API for pulling stats
- **Proxmox API scripts.** PVEAuthCookie auth, mostly bulk actions and status pulls.
- **IoT VLAN buildout notes.** Network segmentation on VLAN 30 (192.168.30.0/24) with zone-based firewall rules between IoT and trusted networks.
- Guest network isolation. Separate SSID on VLAN 2, firewalled off from LAN and management so visitors can hit the internet without touching anything internal.
- **AD lab guide.** Isolated Windows Server 2022 domain lab (ad.adlab.internal) on a private vmbr1 bridge with pfSense as the edge.
- **Raspberry Pi travel router.** Portable WiFi router build for hotels and travel.

## Scope

**In scope**
- Anything I actually run in my homelab.
- Notes and guides written for my own reference.
- Scripts I've tested and use regularly.

**Out of scope**
- Secrets, real hostnames, or anything specific to my private LAN.
- Half-finished experiments I haven't validated.
- Anything I couldn't reproduce cleanly if I rebuilt from scratch.

If a script depends on my environment, I try to call that out in the folder's own README instead of making it a hidden gotcha.

## Homelab context

Some of this only makes sense against the stack it was written for. Current setup:

- Proxmox on a Dell T420 (RAID via PERC H710).
- Docker on an Ubuntu Server VM running Uptime Kuma, Gitea, and Vaultwarden.
- Caddy reverse proxy with wildcard TLS via Cloudflare DNS-01 on andrelab.net.
- Pi-hole with Unbound recursion (plus a Pi-hole LXC as a secondary).
- WireGuard for remote access.
- Cisco 2960-X for switching and CLI practice.

## Requirements

Python 3.10+ for the API scripts. Each project folder has its own README with anything specific to that project.

## Roadmap

Studying for Security+ now, then AWS SAA. Expect this repo to lean more toward cloud and security tooling over time. Likely additions: Terraform modules, some Kubernetes practice manifests, IAM and identity work.

## Contact

GitHub: [@Andre-132](https://github.com/Andre-132)
