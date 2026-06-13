# Deploy Live Reload

Use this reference when a local bridge or MCP connector has been patched and the host may still be running stale code.

This covers DEP-P0-004 plus the deployed lessons about synced folders, stale bytecode, and host process lifetime.

## Cache-bust policy

Preferred order:

1. Set `PYTHONDONTWRITEBYTECODE=1` in the host pack environment, or start Python with `-B`.
2. Expose a lightweight `health` or `version` tool with `version`, `build_stamp`, `built_at`, and `mode`.
3. Only when host env cannot be controlled, set `sys.dont_write_bytecode = True` at the top of the bridge entrypoint.

`build_stamp` must not expose secrets. Use a git revision, source hash, package version plus timestamp, or another non-secret identifier.

## Live reload runbook

1. Verify the source file with the authoritative file tool/editor.
2. If needed, remove `__pycache__` for the bridge package.
3. Confirm sync status when the folder is in OneDrive/Drive or another synced location.
4. Stop the exact old process, not every Python process. On Windows, filter by path or entrypoint:

```powershell
Get-CimInstance Win32_Process -Filter "Name='python.exe'" |
  Where-Object { $_.CommandLine -like '*server.py*' } |
  ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
```

5. Restart the host or connector.
6. Run a read-only acceptance probe through the host and compare `build_stamp`, output shape, and expected tool catalog.

## Mount/sync caveat

A shell mount can disagree with the real filesystem about mtime, deletion, or synced-file state. Treat host live probes and authoritative file-tool reads as stronger evidence than stale mount output.

## Stop rule

Do not claim `fresh_process_validated` or `host_loaded` if the build stamp is missing or mismatched, or if the old process may still be alive.
