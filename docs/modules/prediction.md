# Prediction

## Purpose and location

Forecasting is implemented through the forecast agent and its model-registry, feature, and evidence dependencies. A standalone production prediction service is not claimed by the public interface example.

## Input and output contract

Inputs include coin identity, forecast horizon, current market context, eligible historical data, and any available production model. Outputs identify the method, forecast value, time context, and applicable model/evidence references. Warnings explain degraded paths.

A persistence baseline is a forecast method with a distinct interpretation. It must not be presented as an inference from a learned model. The public [prediction schema](../../schemas/public/prediction-response.json) preserves that distinction while omitting internal database identifiers and implementation-specific fields.

## Registered-model path

The agent obtains a production model, builds the shared feature frame, validates feature version and columns, and attempts prediction. It rejects invalid price outputs and requires decision evidence matching the model and requested scope.

The existence of a production registry row is not sufficient: the artifact must be available, usable, compatible with the feature frame, and associated with matching decision evidence.

## Failure handling

No available production model, inadequate history, compatibility failure, invalid predictions, or evidence-validation failure can lead to explicitly labelled naive persistence. Registry loading can also treat unavailable artifacts as an unavailable model. Forecast records preserve the actual serving path's model association rather than claiming successful learned inference for a baseline.

Missing current price prevents a meaningful forecast; not every failure can be resolved by returning a number. Downstream recommendations must inspect status and warnings rather than only the forecast value.

## Evidence limit

The code establishes a conditional learned-model path and fallback behavior. The selected runtime observations establish registrations and non-promotion decisions. They do not demonstrate successful production ML inference or prove that all registered feature subsets can be served.

The [public example](../../examples/prediction_example.py) only constructs an illustrative response. It does not load a model, run inference, or call the platform.
