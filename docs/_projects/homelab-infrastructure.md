---
title: Homelab Infrastructure
layout: project
---

## Homelab Infrastructure

Self-hosted server architecture built as a live, phased Docker Compose environment for learning, service delivery, monitoring, and automation.

## Problem Solved

The goal was to build a reliable personal infrastructure stack that could run useful services without turning a 16 GB host into an always-on resource bottleneck. The system needed to separate foundational services from heavier workloads, keep administrative surfaces controlled, and make expansion possible as hardware improves.

## Architecture

- **Phase 1 core:** Portainer, Nginx Proxy Manager, Authentik, Homepage, Beszel, Uptime Kuma, Watchtower, Scrutiny, Vaultwarden, ntfy, PostgreSQL, and Redis
- **Phase 2 media/documents:** Jellyfin, Audiobookshelf, Navidrome, Paperless-ngx, Immich, Prowlarr, Bazarr, and gated torrent services
- **Phase 3 AI/gaming/utility:** Ollama with NVIDIA support, Open WebUI, Minecraft, n8n, Home Assistant, Spoolman, Actual Budget, Stirling PDF, IT-Tools, and web games
- **Phase 4 on-demand:** heavier services such as Kasm, Guacamole, Nextcloud, Gitea, Supabase Studio, Kiwix, Docmost, Cal.com, and NocoDB

## Technical Contributions

- Built phased Compose stacks so core infrastructure can stay live while heavy services remain manual or scheduled.
- Centralized databases and cache services where practical to reduce overhead.
- Added resource-aware service metadata for RAM, CPU, GPU, dependency, tier, and schedule planning.
- Documented setup, environment variables, monitoring, service access, backup, and maintenance workflows.
- Included automation for bootstrapping, on-demand service toggling, model selection, backup, monitoring seeding, and Wake-on-LAN behavior.

## Live System Notes

The server is currently live. Public portfolio details intentionally describe architecture and engineering decisions without exposing private hostnames, secrets, internal addresses, or administrative endpoints.

## Why It Matters

This project shows infrastructure judgment: not just getting containers running, but designing for resource limits, service dependency order, identity, observability, backup, and day-to-day maintainability.
