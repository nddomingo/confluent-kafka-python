# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tests/integration/schema_registry/data/proto/metadata_proto.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAtests/integration/schema_registry/data/proto/metadata_proto.proto\x12\x0b\x43riteo.Glup\x1a google/protobuf/descriptor.proto\"$\n\x13KafkaMessageOptions\x12\r\n\x05topic\x18\x01 \x03(\t\"\x80\x02\n\x07\x44\x61taSet\x12\n\n\x02id\x18\x01 \x01(\t\x12*\n\x06\x66ormat\x18\x02 \x03(\x0b\x32\x1a.Criteo.Glup.DataSetFormat\x12\x36\n\x10partition_scheme\x18\x03 \x01(\x0e\x32\x1c.Criteo.Glup.PartitionScheme\x12\x12\n\njava_class\x18\x04 \x01(\t\x12\x11\n\tfor_tests\x18\x05 \x01(\x08\x12\r\n\x05owner\x18\x06 \x01(\t\x12\x0f\n\x07private\x18\x07 \x01(\x08\x12&\n\x04kind\x18\x08 \x01(\x0e\x32\x18.Criteo.Glup.DataSetKind\x12\x16\n\x0eretention_days\x18\t \x01(\x05\"x\n\x0c\x44\x61taSetChunk\x12)\n\tpartition\x18\x01 \x03(\x0b\x32\x16.Criteo.Glup.Partition\x12*\n\x06\x66ormat\x18\x02 \x01(\x0b\x32\x1a.Criteo.Glup.DataSetFormat\x12\x11\n\tdatasetId\x18\x03 \x01(\t\"\xe6\x02\n\rDataSetFormat\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x30\n\x0b\x66ile_format\x18\x02 \x01(\x0e\x32\x1b.Criteo.Glup.HDFSDataFormat\x12\x36\n\x10partition_scheme\x18\x03 \x01(\x0e\x32\x1c.Criteo.Glup.PartitionScheme\x12\x33\n\x0fstart_partition\x18\x04 \x01(\x0b\x32\x1a.Criteo.Glup.HDFSPartition\x12\x31\n\rend_partition\x18\x05 \x01(\x0b\x32\x1a.Criteo.Glup.HDFSPartition\x12\x16\n\x0eretention_days\x18\x07 \x01(\x05\x12\x10\n\x08priority\x18\x08 \x01(\x05\x12\r\n\x05label\x18\t \x01(\t\x12\x36\n\x10monitoring_level\x18\n \x01(\x0e\x32\x1c.Criteo.Glup.MonitoringLevelJ\x04\x08\x06\x10\x07\"\xce\x19\n\x0bHDFSOptions\x12\x36\n\x06import\x18\x03 \x03(\x0b\x32&.Criteo.Glup.HDFSOptions.ImportOptions\x1a\x86\x19\n\rImportOptions\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x32\n\x0cpartitioning\x18\x04 \x01(\x0e\x32\x1c.Criteo.Glup.PartitionScheme\x12+\n\x06\x66ormat\x18\x05 \x01(\x0e\x32\x1b.Criteo.Glup.HDFSDataFormat\x12\x0f\n\x07private\x18\x06 \x01(\x08\x12\x43\n\tgenerator\x18\x0b \x03(\x0b\x32\x30.Criteo.Glup.HDFSOptions.ImportOptions.Generator\x12\x39\n\x04view\x18\x0c \x03(\x0b\x32+.Criteo.Glup.HDFSOptions.ImportOptions.View\x1a\x90\x01\n\x04View\x12\x45\n\x04hive\x18\n \x01(\x0b\x32\x37.Criteo.Glup.HDFSOptions.ImportOptions.View.HiveOptions\x1a\x41\n\x0bHiveOptions\x12\x32\n\x0cpartitioning\x18\x03 \x01(\x0e\x32\x1c.Criteo.Glup.PartitionScheme\x1a\xd2\x15\n\tGenerator\x12V\n\ndataloader\x18\x01 \x01(\x0b\x32\x42.Criteo.Glup.HDFSOptions.ImportOptions.Generator.DataloaderOptions\x12V\n\nkafka2hdfs\x18\x02 \x01(\x0b\x32\x42.Criteo.Glup.HDFSOptions.ImportOptions.Generator.Kafka2HdfsOptions\x12J\n\x04sync\x18\x03 \x01(\x0b\x32<.Criteo.Glup.HDFSOptions.ImportOptions.Generator.SyncOptions\x12R\n\x08\x65xternal\x18\x04 \x01(\x0b\x32@.Criteo.Glup.HDFSOptions.ImportOptions.Generator.ExternalOptions\x12N\n\x06\x62\x61\x63kup\x18\x05 \x01(\x0b\x32>.Criteo.Glup.HDFSOptions.ImportOptions.Generator.BackupOptions\x12X\n\x0btranscoding\x18\x06 \x01(\x0b\x32\x43.Criteo.Glup.HDFSOptions.ImportOptions.Generator.TranscodingOptions\x12N\n\x06kacoha\x18\x07 \x01(\x0b\x32>.Criteo.Glup.HDFSOptions.ImportOptions.Generator.KaCoHaOptions\x12R\n\x0b\x64\x65\x64uplicate\x18\x08 \x01(\x0b\x32=.Criteo.Glup.HDFSOptions.ImportOptions.Generator.DedupOptions\x12P\n\x07sampler\x18\t \x01(\x0b\x32?.Criteo.Glup.HDFSOptions.ImportOptions.Generator.SamplerOptions\x12V\n\ncomparator\x18\n \x01(\x0b\x32\x42.Criteo.Glup.HDFSOptions.ImportOptions.Generator.ComparatorOptions\x12\"\n\x02to\x18\xfa\x01 \x03(\x0b\x32\x15.Criteo.Glup.Location\x12\x12\n\tnamespace\x18\xfb\x01 \x01(\t\x12\x13\n\nstart_date\x18\xfd\x01 \x01(\t\x12\x12\n\tstop_date\x18\xfe\x01 \x01(\t\x12\x12\n\tignore_cn\x18\xff\x01 \x01(\x08\x1a\x9a\x01\n\x0c\x44\x65\x64upOptions\x12\x18\n\x10input_dataset_id\x18\x01 \x01(\t\x12\x1a\n\x12input_format_label\x18\x02 \x01(\t\x12\x19\n\x11output_dataset_id\x18\x03 \x01(\t\x12\x1b\n\x13output_format_label\x18\x04 \x01(\t\x12\x1c\n\x14use_hippo_cuttle_job\x18\x05 \x01(\x08\x1au\n\x11Kafka2HdfsOptions\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65\x64uplicate\x18\x03 \x01(\x08\x12\x19\n\x11output_dataset_id\x18\x04 \x01(\t\x12\x1b\n\x13output_format_label\x18\x05 \x01(\tJ\x04\x08\x02\x10\x03\x1aK\n\x0cKacohaConfig\x12\x1b\n\x13partitions_per_task\x18\x01 \x01(\x05\x12\x1e\n\x16poll_buffer_size_bytes\x18\x02 \x01(\x05\x1a\x87\x01\n\x11KacohaConfigPerDc\x12#\n\x02\x64\x63\x18\x01 \x01(\x0e\x32\x17.Criteo.Glup.DataCenter\x12M\n\x06\x63onfig\x18\x02 \x01(\x0b\x32=.Criteo.Glup.HDFSOptions.ImportOptions.Generator.KacohaConfig\x1a\x95\x02\n\rKaCoHaOptions\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x19\n\x11output_dataset_id\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65\x64uplicate\x18\x03 \x01(\x08\x12M\n\x06\x63onfig\x18\x04 \x01(\x0b\x32=.Criteo.Glup.HDFSOptions.ImportOptions.Generator.KacohaConfig\x12\x1b\n\x13output_format_label\x18\x05 \x01(\t\x12Y\n\rconfig_per_dc\x18\x06 \x03(\x0b\x32\x42.Criteo.Glup.HDFSOptions.ImportOptions.Generator.KacohaConfigPerDc\x1a<\n\x11\x44\x61taloaderOptions\x12\'\n\x08platform\x18\x01 \x03(\x0e\x32\x15.Criteo.Glup.Platform\x1a\xf1\x01\n\x0bSyncOptions\x12#\n\x04\x66rom\x18\x01 \x01(\x0b\x32\x15.Criteo.Glup.Location\x12\x18\n\x10source_namespace\x18\x03 \x01(\t\x12(\n\tplatforms\x18\x06 \x03(\x0e\x32\x15.Criteo.Glup.Platform\x12\x16\n\x0eis_backfilling\x18\x08 \x01(\x08\x12\x10\n\x08to_label\x18\t \x01(\t\x12\x15\n\rto_dataset_id\x18\n \x01(\t\x12\x18\n\x10with_backfilling\x18\x0b \x01(\x08\x12\x1e\n\x16is_scheduled_on_source\x18\x0c \x01(\x08\x1ax\n\rBackupOptions\x12#\n\x04\x66rom\x18\x01 \x01(\x0b\x32\x15.Criteo.Glup.Location\x12\x18\n\x10source_namespace\x18\x02 \x01(\t\x12(\n\tplatforms\x18\x03 \x03(\x0e\x32\x15.Criteo.Glup.Platform\x1a\x83\x02\n\x12TranscodingOptions\x12\x18\n\x10input_dataset_id\x18\x01 \x01(\t\x12\x19\n\x11output_dataset_id\x18\x02 \x01(\t\x12\x31\n\x0cinput_format\x18\x03 \x01(\x0e\x32\x1b.Criteo.Glup.HDFSDataFormat\x12\x32\n\routput_format\x18\x04 \x01(\x0e\x32\x1b.Criteo.Glup.HDFSDataFormat\x12\x1b\n\x13input_dataset_label\x18\x05 \x01(\t\x12\x1c\n\x14output_dataset_label\x18\x06 \x01(\t\x12\x16\n\x0eis_by_platform\x18\x07 \x01(\x08\x1a\x95\x01\n\x0eSamplerOptions\x12\x18\n\x10input_dataset_id\x18\x01 \x01(\t\x12\x1a\n\x12input_format_label\x18\x02 \x01(\t\x12\x19\n\x11output_dataset_id\x18\x03 \x01(\t\x12\x1b\n\x13output_format_label\x18\x04 \x01(\t\x12\x15\n\rsampling_rate\x18\x05 \x01(\x02\x1a\xa7\x01\n\x11\x43omparatorOptions\x12\x17\n\x0fleft_dataset_id\x18\x01 \x01(\t\x12\x19\n\x11left_format_label\x18\x02 \x01(\t\x12\x18\n\x10right_dataset_id\x18\x03 \x01(\t\x12\x1a\n\x12right_format_label\x18\x04 \x01(\t\x12\x10\n\x08hostname\x18\x05 \x01(\t\x12\x16\n\x0eignored_fields\x18\x06 \x01(\t\x1a\x11\n\x0f\x45xternalOptions\"9\n\x18ProducerTransportOptions\x12\x0e\n\x06syslog\x18\x01 \x01(\x08\x12\r\n\x05kafka\x18\x02 \x01(\x08\"8\n\x0fPropertyOptions\x12\x10\n\x08valuable\x18\x01 \x01(\x08\x12\x13\n\x0bhigh_volume\x18\x02 \x01(\x08\"\xcb\x02\n\x0bGlupOptions\x12/\n\x05kafka\x18\x01 \x01(\x0b\x32 .Criteo.Glup.KafkaMessageOptions\x12&\n\x04hdfs\x18\x02 \x01(\x0b\x32\x18.Criteo.Glup.HDFSOptions\x12\x14\n\x0csampling_pct\x18\x03 \x01(\r\x12\x1c\n\x14preprod_sampling_pct\x18\x04 \x01(\r\x12%\n\x07\x64\x61taset\x18\x05 \x03(\x0b\x32\x14.Criteo.Glup.DataSet\x12\x1c\n\x14message_sampling_pct\x18\x06 \x01(\r\x12\x38\n\tproducers\x18\x07 \x01(\x0b\x32%.Criteo.Glup.ProducerTransportOptions\x12\x30\n\nproperties\x18\x08 \x01(\x0b\x32\x1c.Criteo.Glup.PropertyOptions\"\xb1\x01\n\x10GlupFieldOptions\x12\x0f\n\x07sampled\x18\x01 \x01(\x08\x12\x14\n\x0csampling_key\x18\x02 \x01(\x08\x12\x30\n\x11\x64isabled_platform\x18\x03 \x03(\x0e\x32\x15.Criteo.Glup.Platform\x12\x18\n\x10should_clean_pii\x18\x04 \x01(\x08\x12\x18\n\x10pending_deletion\x18\x05 \x01(\x08\x12\x10\n\x08\x61\x64\x64\x65\x64_at\x18\x06 \x01(\t\")\n\x0bJsonMapping\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04skip\x18\x02 \x01(\x08\"4\n\tJsonAlias\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x11use_enum_field_id\x18\x03 \x01(\x08\"\xb5\x02\n\x0f\x42\x61seGlupMessage\x12(\n\x0bglup_origin\x18\x01 \x01(\x0b\x32\x13.Criteo.Glup.Origin\x12)\n\tpartition\x18\x02 \x01(\x0b\x32\x16.Criteo.Glup.Partition\x12\x41\n\nset_fields\x18\xda\x86\x03 \x03(\x0b\x32+.Criteo.Glup.BaseGlupMessage.SetFieldsEntry\x12R\n\x0f\x63ontrol_message\x18\xff\xff\x7f \x03(\x0b\x32%.Criteo.Glup.ControlMessage.WatermarkB\x10\x92\xb5\x18\x0c\n\n__metadata\x1a\x30\n\x0eSetFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01:\x04\x88\xb5\x18\x01\"\xf2\x01\n\x19\x46orwardedWatermarkMessage\x12\x1d\n\x15original_kafka_offset\x18\x05 \x01(\x03\x12\x11\n\ttimestamp\x18\x06 \x01(\x03\x12\x1d\n\x15\x63onsolidation_enabled\x18\x07 \x01(\x08\x12\x12\n\ndataset_id\x18\n \x01(\t\x12\x1c\n\x14\x64\x61taset_format_label\x18\x0b \x01(\t\x12R\n\x0f\x63ontrol_message\x18\xff\xff\x7f \x03(\x0b\x32%.Criteo.Glup.ControlMessage.WatermarkB\x10\x92\xb5\x18\x0c\n\n__metadata\"y\n\x08Location\x12%\n\x03\x65nv\x18\x01 \x01(\x0e\x32\x18.Criteo.Glup.Environment\x12#\n\x02\x64\x63\x18\x02 \x01(\x0e\x32\x17.Criteo.Glup.DataCenter\x12\r\n\x05label\x18\x03 \x01(\t\x12\x12\n\ndataset_id\x18\x04 \x01(\t\"\xa2\x01\n\x06Origin\x12+\n\ndatacenter\x18\x01 \x01(\x0e\x32\x17.Criteo.Glup.DataCenter\x12\x1a\n\x03ip4\x18\x02 \x01(\x07\x42\r\x8a\xb5\x18\t\n\x07host_ip\x12\x10\n\x08hostname\x18\x03 \x01(\t\x12\x1e\n\x0e\x63ontainer_task\x18\x04 \x01(\tB\x06\x8a\xb5\x18\x02\x10\x01\x12\x1d\n\rcontainer_app\x18\x05 \x01(\tB\x06\x8a\xb5\x18\x02\x10\x01\"\x89\x05\n\x0e\x43ontrolMessage\x12\x38\n\twatermark\x18\x01 \x01(\x0b\x32%.Criteo.Glup.ControlMessage.Watermark\x1a\x89\x01\n\x0fWatermarkOrigin\x12\x13\n\x0bkafka_topic\x18\x01 \x01(\t\x12+\n\ndatacenter\x18\x02 \x01(\x0e\x32\x17.Criteo.Glup.DataCenter\x12\x34\n\x07\x63luster\x18\x03 \x01(\x0e\x32#.Criteo.Glup.ControlMessage.Cluster\x1a\xe8\x02\n\tWatermark\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08hostname\x18\x02 \x01(\t\x12\x13\n\x0bkafka_topic\x18\x03 \x01(\t\x12\x11\n\tpartition\x18\x04 \x01(\x05\x12\x17\n\x0fpartition_count\x18\x05 \x01(\x05\x12\x14\n\x0cprocess_uuid\x18\x06 \x01(\x0c\x12\x0e\n\x06region\x18\x07 \x01(\t\x12*\n\x11timestamp_seconds\x18\x08 \x01(\x05\x42\x0f\x92\xb5\x18\x0b\n\ttimestamp\x12\x0f\n\x07\x63luster\x18\t \x01(\t\x12\x13\n\x0b\x65nvironment\x18\n \x01(\t\x12J\n\nset_fields\x18\xda\x86\x03 \x03(\x0b\x32\x34.Criteo.Glup.ControlMessage.Watermark.SetFieldsEntry\x1a\x30\n\x0eSetFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01:\x04\x88\xb5\x18\x01\"F\n\x07\x43luster\x12\x17\n\x13UNSUPPORTED_CLUSTER\x10\x00\x12\t\n\x05LOCAL\x10\x02\x12\x0b\n\x07\x43\x45NTRAL\x10\x03\x12\n\n\x06STREAM\x10\x04\"\x99\x01\n\tPartition\x12*\n\x11timestamp_seconds\x18\x01 \x01(\x04\x42\x0f\x8a\xb5\x18\x0b\n\ttimestamp\x12,\n\rhost_platform\x18\x02 \x01(\x0e\x32\x15.Criteo.Glup.Platform\x12\x32\n\nevent_type\x18\x03 \x01(\x0e\x32\x16.Criteo.Glup.EventTypeB\x06\x8a\xb5\x18\x02\x10\x01\"\x93\x01\n\rHDFSPartition\x12\x19\n\x11timestamp_seconds\x18\x01 \x01(\x04\x12,\n\rhost_platform\x18\x02 \x01(\x0e\x32\x15.Criteo.Glup.Platform\x12*\n\nevent_type\x18\x03 \x01(\x0e\x32\x16.Criteo.Glup.EventType\x12\r\n\x05\x64\x65pth\x18\x04 \x01(\x05\"\xa5\x01\n\x07Hash128\x12\x15\n\rmost_sig_bits\x18\x01 \x01(\x06\x12\x16\n\x0eleast_sig_bits\x18\x02 \x01(\x06\x12\x39\n\nset_fields\x18\xda\x86\x03 \x03(\x0b\x32#.Criteo.Glup.Hash128.SetFieldsEntry\x1a\x30\n\x0eSetFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01*~\n\x0fPartitionScheme\x12 \n\x1cUNSUPPORTED_PARTITION_SCHEME\x10\x00\x12\t\n\x05\x44\x41ILY\x10\x02\x12\n\n\x06HOURLY\x10\x03\x12\x13\n\x0fPLATFORM_HOURLY\x10\x04\x12\x1d\n\x19\x45VENTTYPE_PLATFORM_HOURLY\x10\x05*?\n\rMessageFormat\x12\x16\n\x12UNSUPPORTED_FORMAT\x10\x00\x12\x08\n\x04JSON\x10\x01\x12\x0c\n\x08PROTOBUF\x10\x02*d\n\x0eHDFSDataFormat\x12\x1b\n\x17UNSUPPORTED_DATA_FORMAT\x10\x00\x12\r\n\tJSON_PAIL\x10\x02\x12\x10\n\x0cPROTOBUF_SEQ\x10\x03\x12\x14\n\x10PROTOBUF_PARQUET\x10\x04*3\n\x0b\x44\x61taSetKind\x12\x14\n\x10UNSUPPORTED_KIND\x10\x00\x12\x0e\n\nTIMESERIES\x10\x01*\x9a\x01\n\x0fMonitoringLevel\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x15\n\x11REMOVE_MONITORING\x10\x01\x12\x1a\n\x16INFORMATIVE_MONITORING\x10\x02\x12\x15\n\x11\x43ONSENSUS_IGNORED\x10\x03\x12\x30\n,CONSENSUS_IGNORED_AND_INFORMATIVE_MONITORING\x10\x04*\x8b\x01\n\nDataCenter\x12\x1a\n\x16UNSUPPORTED_DATACENTER\x10\x00\x12\x07\n\x03\x41M5\x10\x02\x12\x07\n\x03HK5\x10\x03\x12\x07\n\x03NY8\x10\x04\x12\x07\n\x03PAR\x10\x05\x12\x07\n\x03PA4\x10\x06\x12\x07\n\x03SH5\x10\x07\x12\x07\n\x03SV6\x10\x08\x12\x07\n\x03TY5\x10\t\x12\x07\n\x03VA1\x10\n\x12\x07\n\x03\x41M6\x10\x0b\x12\x07\n\x03\x44\x41\x31\x10\x0c*A\n\x0b\x45nvironment\x12\x1b\n\x17UNSUPPORTED_ENVIRONMENT\x10\x00\x12\x0b\n\x07PREPROD\x10\x01\x12\x08\n\x04PROD\x10\x02*D\n\x08Platform\x12\x18\n\x14UNSUPPORTED_PLATFORM\x10\x00\x12\x06\n\x02\x45U\x10\x02\x12\x06\n\x02US\x10\x03\x12\x06\n\x02\x41S\x10\x04\x12\x06\n\x02\x43N\x10\x05*[\n\tEventType\x12\x1a\n\x16UNSUPPORTED_EVENT_TYPE\x10\x00\x12\x10\n\x0cItemPageView\x10\x02\x12\t\n\x05Sales\x10\x03\x12\n\n\x06\x42\x61sket\x10\x04\x12\t\n\x05Other\x10\x05*%\n\x05YesNo\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02NO\x10\x01\x12\x07\n\x03YES\x10\x02:I\n\x04glup\x12\x1f.google.protobuf.MessageOptions\x18\xd0\x86\x03 \x01(\x0b\x32\x18.Criteo.Glup.GlupOptions:C\n\x18\x63ontains_nullable_fields\x12\x1f.google.protobuf.MessageOptions\x18\xd1\x86\x03 \x01(\x08:Q\n\tglupfield\x12\x1d.google.protobuf.FieldOptions\x18\xd0\x86\x03 \x01(\x0b\x32\x1d.Criteo.Glup.GlupFieldOptions:O\n\x0cjson_mapping\x12\x1d.google.protobuf.FieldOptions\x18\xd1\x86\x03 \x01(\x0b\x32\x18.Criteo.Glup.JsonMapping:E\n\x04json\x12\x1d.google.protobuf.FieldOptions\x18\xd2\x86\x03 \x01(\x0b\x32\x16.Criteo.Glup.JsonAliasB\x11\n\x0f\x63om.criteo.glupb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tests.integration.schema_registry.data.proto.metadata_proto_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(glup)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(contains_nullable_fields)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(glupfield)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(json_mapping)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(json)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.criteo.glup'
  _BASEGLUPMESSAGE_SETFIELDSENTRY._options = None
  _BASEGLUPMESSAGE_SETFIELDSENTRY._serialized_options = b'8\001'
  _BASEGLUPMESSAGE.fields_by_name['control_message']._options = None
  _BASEGLUPMESSAGE.fields_by_name['control_message']._serialized_options = b'\222\265\030\014\n\n__metadata'
  _BASEGLUPMESSAGE._options = None
  _BASEGLUPMESSAGE._serialized_options = b'\210\265\030\001'
  _FORWARDEDWATERMARKMESSAGE.fields_by_name['control_message']._options = None
  _FORWARDEDWATERMARKMESSAGE.fields_by_name['control_message']._serialized_options = b'\222\265\030\014\n\n__metadata'
  _ORIGIN.fields_by_name['ip4']._options = None
  _ORIGIN.fields_by_name['ip4']._serialized_options = b'\212\265\030\t\n\007host_ip'
  _ORIGIN.fields_by_name['container_task']._options = None
  _ORIGIN.fields_by_name['container_task']._serialized_options = b'\212\265\030\002\020\001'
  _ORIGIN.fields_by_name['container_app']._options = None
  _ORIGIN.fields_by_name['container_app']._serialized_options = b'\212\265\030\002\020\001'
  _CONTROLMESSAGE_WATERMARK_SETFIELDSENTRY._options = None
  _CONTROLMESSAGE_WATERMARK_SETFIELDSENTRY._serialized_options = b'8\001'
  _CONTROLMESSAGE_WATERMARK.fields_by_name['timestamp_seconds']._options = None
  _CONTROLMESSAGE_WATERMARK.fields_by_name['timestamp_seconds']._serialized_options = b'\222\265\030\013\n\ttimestamp'
  _CONTROLMESSAGE_WATERMARK._options = None
  _CONTROLMESSAGE_WATERMARK._serialized_options = b'\210\265\030\001'
  _PARTITION.fields_by_name['timestamp_seconds']._options = None
  _PARTITION.fields_by_name['timestamp_seconds']._serialized_options = b'\212\265\030\013\n\ttimestamp'
  _PARTITION.fields_by_name['event_type']._options = None
  _PARTITION.fields_by_name['event_type']._serialized_options = b'\212\265\030\002\020\001'
  _HASH128_SETFIELDSENTRY._options = None
  _HASH128_SETFIELDSENTRY._serialized_options = b'8\001'
  _PARTITIONSCHEME._serialized_start=6876
  _PARTITIONSCHEME._serialized_end=7002
  _MESSAGEFORMAT._serialized_start=7004
  _MESSAGEFORMAT._serialized_end=7067
  _HDFSDATAFORMAT._serialized_start=7069
  _HDFSDATAFORMAT._serialized_end=7169
  _DATASETKIND._serialized_start=7171
  _DATASETKIND._serialized_end=7222
  _MONITORINGLEVEL._serialized_start=7225
  _MONITORINGLEVEL._serialized_end=7379
  _DATACENTER._serialized_start=7382
  _DATACENTER._serialized_end=7521
  _ENVIRONMENT._serialized_start=7523
  _ENVIRONMENT._serialized_end=7588
  _PLATFORM._serialized_start=7590
  _PLATFORM._serialized_end=7658
  _EVENTTYPE._serialized_start=7660
  _EVENTTYPE._serialized_end=7751
  _YESNO._serialized_start=7753
  _YESNO._serialized_end=7790
  _KAFKAMESSAGEOPTIONS._serialized_start=116
  _KAFKAMESSAGEOPTIONS._serialized_end=152
  _DATASET._serialized_start=155
  _DATASET._serialized_end=411
  _DATASETCHUNK._serialized_start=413
  _DATASETCHUNK._serialized_end=533
  _DATASETFORMAT._serialized_start=536
  _DATASETFORMAT._serialized_end=894
  _HDFSOPTIONS._serialized_start=897
  _HDFSOPTIONS._serialized_end=4175
  _HDFSOPTIONS_IMPORTOPTIONS._serialized_start=969
  _HDFSOPTIONS_IMPORTOPTIONS._serialized_end=4175
  _HDFSOPTIONS_IMPORTOPTIONS_VIEW._serialized_start=1258
  _HDFSOPTIONS_IMPORTOPTIONS_VIEW._serialized_end=1402
  _HDFSOPTIONS_IMPORTOPTIONS_VIEW_HIVEOPTIONS._serialized_start=1337
  _HDFSOPTIONS_IMPORTOPTIONS_VIEW_HIVEOPTIONS._serialized_end=1402
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR._serialized_start=1405
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR._serialized_end=4175
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_DEDUPOPTIONS._serialized_start=2376
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_DEDUPOPTIONS._serialized_end=2530
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_KAFKA2HDFSOPTIONS._serialized_start=2532
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_KAFKA2HDFSOPTIONS._serialized_end=2649
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_KACOHACONFIG._serialized_start=2651
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_KACOHACONFIG._serialized_end=2726
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_KACOHACONFIGPERDC._serialized_start=2729
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_KACOHACONFIGPERDC._serialized_end=2864
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_KACOHAOPTIONS._serialized_start=2867
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_KACOHAOPTIONS._serialized_end=3144
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_DATALOADEROPTIONS._serialized_start=3146
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_DATALOADEROPTIONS._serialized_end=3206
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_SYNCOPTIONS._serialized_start=3209
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_SYNCOPTIONS._serialized_end=3450
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_BACKUPOPTIONS._serialized_start=3452
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_BACKUPOPTIONS._serialized_end=3572
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_TRANSCODINGOPTIONS._serialized_start=3575
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_TRANSCODINGOPTIONS._serialized_end=3834
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_SAMPLEROPTIONS._serialized_start=3837
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_SAMPLEROPTIONS._serialized_end=3986
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_COMPARATOROPTIONS._serialized_start=3989
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_COMPARATOROPTIONS._serialized_end=4156
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_EXTERNALOPTIONS._serialized_start=4158
  _HDFSOPTIONS_IMPORTOPTIONS_GENERATOR_EXTERNALOPTIONS._serialized_end=4175
  _PRODUCERTRANSPORTOPTIONS._serialized_start=4177
  _PRODUCERTRANSPORTOPTIONS._serialized_end=4234
  _PROPERTYOPTIONS._serialized_start=4236
  _PROPERTYOPTIONS._serialized_end=4292
  _GLUPOPTIONS._serialized_start=4295
  _GLUPOPTIONS._serialized_end=4626
  _GLUPFIELDOPTIONS._serialized_start=4629
  _GLUPFIELDOPTIONS._serialized_end=4806
  _JSONMAPPING._serialized_start=4808
  _JSONMAPPING._serialized_end=4849
  _JSONALIAS._serialized_start=4851
  _JSONALIAS._serialized_end=4903
  _BASEGLUPMESSAGE._serialized_start=4906
  _BASEGLUPMESSAGE._serialized_end=5215
  _BASEGLUPMESSAGE_SETFIELDSENTRY._serialized_start=5161
  _BASEGLUPMESSAGE_SETFIELDSENTRY._serialized_end=5209
  _FORWARDEDWATERMARKMESSAGE._serialized_start=5218
  _FORWARDEDWATERMARKMESSAGE._serialized_end=5460
  _LOCATION._serialized_start=5462
  _LOCATION._serialized_end=5583
  _ORIGIN._serialized_start=5586
  _ORIGIN._serialized_end=5748
  _CONTROLMESSAGE._serialized_start=5751
  _CONTROLMESSAGE._serialized_end=6400
  _CONTROLMESSAGE_WATERMARKORIGIN._serialized_start=5828
  _CONTROLMESSAGE_WATERMARKORIGIN._serialized_end=5965
  _CONTROLMESSAGE_WATERMARK._serialized_start=5968
  _CONTROLMESSAGE_WATERMARK._serialized_end=6328
  _CONTROLMESSAGE_WATERMARK_SETFIELDSENTRY._serialized_start=5161
  _CONTROLMESSAGE_WATERMARK_SETFIELDSENTRY._serialized_end=5209
  _CONTROLMESSAGE_CLUSTER._serialized_start=6330
  _CONTROLMESSAGE_CLUSTER._serialized_end=6400
  _PARTITION._serialized_start=6403
  _PARTITION._serialized_end=6556
  _HDFSPARTITION._serialized_start=6559
  _HDFSPARTITION._serialized_end=6706
  _HASH128._serialized_start=6709
  _HASH128._serialized_end=6874
  _HASH128_SETFIELDSENTRY._serialized_start=5161
  _HASH128_SETFIELDSENTRY._serialized_end=5209
# @@protoc_insertion_point(module_scope)
