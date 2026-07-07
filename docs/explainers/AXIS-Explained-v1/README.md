# AXIS Açıklama Paketi v1

Bu klasör, VARUX AXIS'in mevcut repo davranışına dayalı sade ve teknik Türkçe açıklama paketidir. Amaç; bir teknik reviewer'ın, mühendis adayının, müşteri adayının veya kurucunun AXIS'in ne yaptığını, ne yapmadığını, hangi güvenlik modeline dayandığını ve hangi sınırlara sahip olduğunu hızlıca anlayabilmesidir.

Bu paket reklam metni değildir. Mevcut runtime/source dosyalarına dokunmadan, ayrı bir dokümantasyon katmanı olarak hazırlanmıştır.

## AXIS tek cümlede

AXIS, production veritabanı operasyonlarını çalışmadan önce politika ile değerlendiren ve her kritik karar için doğrulanabilir audit evidence üreten deterministik bir kontrol katmanıdır.

## 5 dakikada AXIS

AXIS'i production PostgreSQL önünde çalışan kontrollü bir karar katmanı gibi düşünün:

1. Uygulama, internal tool, script, AI agent veya servis AXIS'e SQL isteği gönderir.
2. AXIS isteği doğrular, SQL'i parse eder ve sınıflandırır.
3. Policy engine, aktif policy'ye göre `ALLOW`, `BLOCK` veya `REQUIRE_APPROVAL` kararı üretir.
4. `ALLOW` ise işlem PostgreSQL'e gönderilir.
5. `BLOCK` ise işlem PostgreSQL'e ulaşmaz.
6. `REQUIRE_APPROVAL` ise approval kaydı oluşur; işlem onay ve aynı bağlamla tekrar gönderim olmadan çalışmaz.
7. Kritik kararlar WAL tabanlı audit evidence olarak yazılır.
8. Evidence, `event_hash` ve `previous_hash` zinciri ile doğrulanabilir.

Not: Bu dokümanda `APPROVAL_REQUIRED` kavramsal ad olarak kullanılır. Mevcut Rust API'sinde aynı karar çoğunlukla `REQUIRE_APPROVAL` olarak serileşir; policy deserialization tarafında `APPROVAL_REQUIRED` alias'ı da desteklenir.

## Okuma sırası

| Sıra | Dosya | Ne anlatır? |
|---:|---|---|
| 1 | [00-AXIS-NEDIR.md](00-AXIS-NEDIR.md) | AXIS'in tanımı, çözdüğü problem ve ne olmadığı |
| 2 | [01-ZIHINSEL-MODEL.md](01-ZIHINSEL-MODEL.md) | Yeni başlayan için profesyonel zihinsel model |
| 3 | [02-POLICY-BEFORE-EXECUTION.md](02-POLICY-BEFORE-EXECUTION.md) | Execution öncesi policy kararının neden temel prensip olduğu |
| 4 | [03-MIMARI-HARITA.md](03-MIMARI-HARITA.md) | Ana mimari katmanlar ve sorumluluklar |
| 5 | [04-KARAR-AKISI.md](04-KARAR-AKISI.md) | SQL isteğinin karara dönüşmesi |
| 6 | [05-ONAY-AKISI.md](05-ONAY-AKISI.md) | Approval yaşam döngüsü |
| 7 | [06-AUDIT-EVIDENCE.md](06-AUDIT-EVIDENCE.md) | WAL, JSONL projection, hash chain ve export |
| 8 | [07-FAIL-SAFE-DAVRANIS.md](07-FAIL-SAFE-DAVRANIS.md) | Fail-safe ve fail-closed davranışlar |
| 9 | [08-POLICY-YASAM-DONGUSU-VE-BUTUNLUK.md](08-POLICY-YASAM-DONGUSU-VE-BUTUNLUK.md) | Manifest, SHA-256, dry-run, activation ve rollback |
| 10 | [09-GUVEN-SINIRLARI.md](09-GUVEN-SINIRLARI.md) | Trusted/untrusted sınırlar |
| 11 | [10-RUNTIME-AKISLARI.md](10-RUNTIME-AKISLARI.md) | Ayrı runtime akışları |
| 12 | [11-HATA-MODU-MATRISI.md](11-HATA-MODU-MATRISI.md) | Hata senaryoları ve beklenen davranışlar |
| 13 | [12-REVIEWER-REHBERI.md](12-REVIEWER-REHBERI.md) | Teknik reviewer için doğrulama rehberi |
| 14 | [13-MUSTERI-ICIN-TEKNIK-ANLATIM.md](13-MUSTERI-ICIN-TEKNIK-ANLATIM.md) | Müşteri adayına teknik anlatım |
| 15 | [14-HEDEF-OLMAYANLAR-VE-LIMITLER.md](14-HEDEF-OLMAYANLAR-VE-LIMITLER.md) | Açık non-goals ve limitler |
| 16 | [15-SOZLUK.md](15-SOZLUK.md) | Terimler sözlüğü |
| 17 | [CHECKLIST.md](CHECKLIST.md) | Paket kalite kontrol listesi |

## Diyagramlar

Mermaid kaynakları [diagrams/](diagrams/) altında ayrı dosya olarak tutulur. Tek başına açılabilir HTML görseli [visual/axis-map.html](visual/axis-map.html) içindedir ve harici dependency kullanmaz.

## Uygulandı, kavramsal, gelecek çalışma ayrımı

Bu paketteki anlatım mevcut repo içindeki Rust backend, policy lifecycle, approval store, audit WAL, evidence verification, Control Plane proxy ve pilot dokümanlarına göre yazılmıştır.

Kavramsal ifadeler özellikle işaretlenir. Örneğin `SUSPEND`, mevcut kaynakta ayrı bir policy enum değeri değildir; approval veya belirsiz execution durumlarında kullanılan askıya alma davranışını anlatan kavramsal bir terimdir. Native PostgreSQL wire protocol desteği de mevcut HTTP adapter modelinden ayrı değerlendirilmelidir.

