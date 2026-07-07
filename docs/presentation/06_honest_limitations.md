# Dürüst Sınırlar

Bu bolum bilincli olarak dahil edildi cunku net sinirlar belirsiz iddialardan daha guvenilirdir.

## Stored Function Ve Procedure Govdeleri Opaktır

- AXIS, client'in gonderdigi SQL metnini gorur.
- Onceden veritabaninda tanimlanmis function veya procedure govdesinin icini wire seviyesinde goremez.
- Bu AXIS'e ozgu bir eksik degil; PostgreSQL wire seviyesinde calisan benzer proxy'ler icin mimari sinirdir.
- Repo, bu davranisi regression test ile dogruluyor: function govdesinde veri silme olsa bile AXIS sadece function cagrisini policy'ler.
- Tamamlayici kontrol: PostgreSQL'in native GRANT ve REVOKE mekanizmalariyla function/procedure olusturma ve calistirma yetkileri kisitlanmalidir.

## COPY Protokolü Desteklenmiyor

- COPY FROM STDIN, COPY TO STDOUT ve CopyData alt-protokolu pgwire modunda desteklenmiyor.
- Beklenen davranis fail-closed: AXIS bulk data aktarimina girmeden reddeder.
- Repo testleri COPY FROM, COPY TO ve COPY reddi sonrasi baglanti kullanilabilirligi icin regression coverage iceriyor.

## JDBC Batch Ve Genel Pipelining Siniri

- pgjdbc batch execution MVP kapsaminda desteklenmiyor.
- Bunun nedeni ayni protocol cycle icinde birden fazla Bind/Execute akisinin ileri faz karari olarak ayrilmis olmasidir.
- Driver matrix bu davranisi desteklenmis gibi gostermiyor; temiz 42501 reddi ve baglanti kullanilabilirligi olarak belgeliyor.
- PIPELINING_SUPPORT=false iken JDBC batch yesil destek olarak isaretlenmemeli.

## Hassas Session Parametreleri Reddedilir

- search_path, role, session_authorization ve row_security reddedilir.
- Bunlari whitelist'e almak ayri bir guvenlik incelemesi ve bypass analizi gerektirir.
- search_path ozellikle hassastir; cunku unqualified tablo ve function isimlerinin PostgreSQL icinde nereye cozuldugunu degistirir.

## Deployment Sinirlari

- AXIS, kendisini tamamen bypass eden veritabani trafigini koruyamaz.
- Pilot veya uretim ortaminda ag, IAM, firewall, security group ve veritabani erisim kontrolleri AXIS'in zorunlu yol olmasini saglamalidir.
- Repo, full RBAC, SSO, TLS/mTLS deployment story, external KMS, external tamper-proof ledger veya multi-instance consensus'u bugunku kanitli uretim ozelligi olarak sunmuyor.
