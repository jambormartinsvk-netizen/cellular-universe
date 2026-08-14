# Package tree seal — EA-20260717-005

**State:** `SEALED_READY_FOR_AUDIT`  
**Sealed:** 2026-07-17  
**Files covered:** `46`  
**Excluded:** iba tento súbor `06_PACKAGE_TREE_SEAL.md`

## Canonical tree SHA-256

```text
6EAB8B2AD1AADE9CD24DDCEBE2698E5F223D475F877CFB78F57BEAE4B328E55F
```

## Canonical serialization

Pre každý zahrnutý súbor sa vytvorí riadok:

```text
relative/path/with/forward/slashes<TAB>UPPERCASE_SHA256<LF>
```

Riadky sa zoradia ordinalne podľa relatívnej cesty, spoja sa bez BOM v
UTF-8 a výsledný text končí jedným `LF`. Uvedený tree hash je SHA-256 tohto
textu.

SHA-256 ľudského manifestu pri sealovaní:

```text
8685A02D60746471F6FA4946485412C06C23A8172837CBDE660220566B093108
```

Po vytvorení tohto sealu sa balík nesmie meniť. Oprava vyžaduje nový
Package ID.
