# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/resources/keyword_plan_campaign.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.enums import keyword_plan_network_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_keyword__plan__network__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/resources/keyword_plan_campaign.proto',
  package='google.ads.googleads.v3.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v3.resourcesB\030KeywordPlanCampaignProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V3.Resources\312\002!Google\\Ads\\GoogleAds\\V3\\Resources\352\002%Google::Ads::GoogleAds::V3::Resources'),
  serialized_pb=_b('\nCgoogle/ads/googleads_v3/proto/resources/keyword_plan_campaign.proto\x12!google.ads.googleads.v3.resources\x1a>google/ads/googleads_v3/proto/enums/keyword_plan_network.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xd0\x04\n\x13KeywordPlanCampaign\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x32\n\x0ckeyword_plan\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\'\n\x02id\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12*\n\x04name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x12language_constants\x18\x05 \x03(\x0b\x32\x1c.google.protobuf.StringValue\x12\x66\n\x14keyword_plan_network\x18\x06 \x01(\x0e\x32H.google.ads.googleads.v3.enums.KeywordPlanNetworkEnum.KeywordPlanNetwork\x12\x33\n\x0e\x63pc_bid_micros\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12L\n\x0bgeo_targets\x18\x08 \x03(\x0b\x32\x37.google.ads.googleads.v3.resources.KeywordPlanGeoTarget:t\xea\x41q\n,googleads.googleapis.com/KeywordPlanCampaign\x12\x41\x63ustomers/{customer}/keywordPlanCampaigns/{keyword_plan_campaign}\"Q\n\x14KeywordPlanGeoTarget\x12\x39\n\x13geo_target_constant\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x85\x02\n%com.google.ads.googleads.v3.resourcesB\x18KeywordPlanCampaignProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V3.Resources\xca\x02!Google\\Ads\\GoogleAds\\V3\\Resources\xea\x02%Google::Ads::GoogleAds::V3::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_keyword__plan__network__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_KEYWORDPLANCAMPAIGN = _descriptor.Descriptor(
  name='KeywordPlanCampaign',
  full_name='google.ads.googleads.v3.resources.KeywordPlanCampaign',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.resources.KeywordPlanCampaign.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword_plan', full_name='google.ads.googleads.v3.resources.KeywordPlanCampaign.keyword_plan', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v3.resources.KeywordPlanCampaign.id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v3.resources.KeywordPlanCampaign.name', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language_constants', full_name='google.ads.googleads.v3.resources.KeywordPlanCampaign.language_constants', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword_plan_network', full_name='google.ads.googleads.v3.resources.KeywordPlanCampaign.keyword_plan_network', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpc_bid_micros', full_name='google.ads.googleads.v3.resources.KeywordPlanCampaign.cpc_bid_micros', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='geo_targets', full_name='google.ads.googleads.v3.resources.KeywordPlanCampaign.geo_targets', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\352Aq\n,googleads.googleapis.com/KeywordPlanCampaign\022Acustomers/{customer}/keywordPlanCampaigns/{keyword_plan_campaign}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=260,
  serialized_end=852,
)


_KEYWORDPLANGEOTARGET = _descriptor.Descriptor(
  name='KeywordPlanGeoTarget',
  full_name='google.ads.googleads.v3.resources.KeywordPlanGeoTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='geo_target_constant', full_name='google.ads.googleads.v3.resources.KeywordPlanGeoTarget.geo_target_constant', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=854,
  serialized_end=935,
)

_KEYWORDPLANCAMPAIGN.fields_by_name['keyword_plan'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_KEYWORDPLANCAMPAIGN.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_KEYWORDPLANCAMPAIGN.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_KEYWORDPLANCAMPAIGN.fields_by_name['language_constants'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_KEYWORDPLANCAMPAIGN.fields_by_name['keyword_plan_network'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_keyword__plan__network__pb2._KEYWORDPLANNETWORKENUM_KEYWORDPLANNETWORK
_KEYWORDPLANCAMPAIGN.fields_by_name['cpc_bid_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_KEYWORDPLANCAMPAIGN.fields_by_name['geo_targets'].message_type = _KEYWORDPLANGEOTARGET
_KEYWORDPLANGEOTARGET.fields_by_name['geo_target_constant'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['KeywordPlanCampaign'] = _KEYWORDPLANCAMPAIGN
DESCRIPTOR.message_types_by_name['KeywordPlanGeoTarget'] = _KEYWORDPLANGEOTARGET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeywordPlanCampaign = _reflection.GeneratedProtocolMessageType('KeywordPlanCampaign', (_message.Message,), dict(
  DESCRIPTOR = _KEYWORDPLANCAMPAIGN,
  __module__ = 'google.ads.googleads_v3.proto.resources.keyword_plan_campaign_pb2'
  ,
  __doc__ = """A Keyword Plan campaign. Max number of keyword plan campaigns per plan
  allowed: 1.
  
  
  Attributes:
      resource_name:
          The resource name of the Keyword Plan campaign.
          KeywordPlanCampaign resource names have the form:  ``customers
          /{customer_id}/keywordPlanCampaigns/{kp_campaign_id}``
      keyword_plan:
          The keyword plan this campaign belongs to.
      id:
          The ID of the Keyword Plan campaign.
      name:
          The name of the Keyword Plan campaign.  This field is required
          and should not be empty when creating Keyword Plan campaigns.
      language_constants:
          The languages targeted for the Keyword Plan campaign. Max
          allowed: 1.
      keyword_plan_network:
          Targeting network.  This field is required and should not be
          empty when creating Keyword Plan campaigns.
      cpc_bid_micros:
          A default max cpc bid in micros, and in the account currency,
          for all ad groups under the campaign.  This field is required
          and should not be empty when creating Keyword Plan campaigns.
      geo_targets:
          The geo targets. Max number allowed: 20.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.resources.KeywordPlanCampaign)
  ))
_sym_db.RegisterMessage(KeywordPlanCampaign)

KeywordPlanGeoTarget = _reflection.GeneratedProtocolMessageType('KeywordPlanGeoTarget', (_message.Message,), dict(
  DESCRIPTOR = _KEYWORDPLANGEOTARGET,
  __module__ = 'google.ads.googleads_v3.proto.resources.keyword_plan_campaign_pb2'
  ,
  __doc__ = """A geo target. Next ID: 3
  
  
  Attributes:
      geo_target_constant:
          Required. The resource name of the geo target.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.resources.KeywordPlanGeoTarget)
  ))
_sym_db.RegisterMessage(KeywordPlanGeoTarget)


DESCRIPTOR._options = None
_KEYWORDPLANCAMPAIGN._options = None
# @@protoc_insertion_point(module_scope)