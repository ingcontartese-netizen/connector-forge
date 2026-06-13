# HOST_BUSY / App Idle Recovery

Use this reference for desktop or local apps that can be busy with user input, locks, modal dialogs, active commands, or document transactions.

`HOST_BUSY` is a typed host state, not a generic connector failure.

## Pattern

1. Run a lightweight ready probe when available.
2. If the app reports user input, modal, lock, transaction, or active command, return `HOST_BUSY`.
3. Retry only with a bounded short backoff.
4. If still busy, ask the user to finish the command, close the modal, save/commit, or press Esc.
5. Re-run the ready probe before retrying the read/write.

## Rules

- Do not force a write while the app is busy.
- Do not treat `HOST_BUSY` as object-not-found or schema failure.
- Use foreground UI automation only with explicit user approval.
- Record the busy recovery in acceptance evidence when desktop/local app readiness is in scope.

## Evidence

Acceptance evidence should include:

- original typed error;
- ready probe result;
- user recovery instruction or bounded retry transcript;
- successful follow-up readback when recovered.

## Failure Rule

If the app cannot reach idle state, stop with `HOLD` or `BLOCKED`. Do not continue blind.
